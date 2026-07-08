/* Kitchen UI helpers — looks normal; talks to /api */
(function () {
  function qs(sel, root) {
    return (root || document).querySelector(sel);
  }

  function starHtml(rating) {
    var full = Math.floor(Number(rating) || 0);
    var html = "";
    for (var i = 1; i <= 5; i++) {
      html +=
        '<i class="fa fa-star' +
        (i > full ? " op5" : "") +
        '"></i>';
    }
    return html;
  }

  function avatarSrc(path) {
    if (!path) path = "table/Untitled-1.jpg";
    return "/static/rubber_duck_pizzeria/images/" + path.replace(/^\/+/, "");
  }

  function reviewCard(rev, idx) {
    var rating = rev.rating != null ? rev.rating : "";
    // Stored XSS sink: body inserted as HTML on purpose
    return (
      '<div class="card review-table p-0 border-0 border-bottom">' +
      '<div class="row align-items-center py-4 px-4">' +
      '<div class="col-xl-4 col-xxl-4 col-lg-5 col-md-12">' +
      '<div class="media align-items-center">' +
      '<div class="form-check custom-checkbox me-2">' +
      '<input type="checkbox" class="form-check-input" id="gridCheck' +
      idx +
      '">' +
      '<label class="form-check-label" for="gridCheck' +
      idx +
      '"></label></div>' +
      '<img class="me-3 img-fluid" width="100" src="' +
      avatarSrc(rev.avatar_path) +
      '" alt="Customer review">' +
      '<div class="card-body p-0">' +
      '<p class="text-primary fs-14 mb-0">' +
      (rev.review_code || "") +
      "</p>" +
      '<h3 class="fs-18 text-black font-w600 mb-2">' +
      (rev.customer_name || "Guest") +
      "</h3>" +
      '<span class="text-dark fs-14">' +
      (rev.created_at || "") +
      "</span></div></div></div>" +
      '<div class="col-xl-5 col-xxl-4 col-lg-7 col-md-12 mt-3 mt-lg-0">' +
      '<p class="mb-0 text-dark">' +
      (rev.body || "") +
      "</p></div>" +
      '<div class="col-xl-3 col-xxl-4 col-lg-7 col-md-12 offset-lg-5 offset-xl-0 mt-xl-0 mt-3">' +
      '<div class="row align-items-center gx-4">' +
      '<div class="text-xl-center start-bx col-xl-7 col-sm-9 col-lg-8 col-6">' +
      '<h2 class="text-black font-w600 me-xl-0 me-3">' +
      rating +
      "</h2>" +
      '<div class="star-review2 mb-2">' +
      starHtml(rating) +
      "</div></div>" +
      '<div class="col-xl-5 col-sm-3 col-lg-4 col-6 text-end">' +
      '<a href="javascript:void(0);" class="text-danger me-2 fs-14 font-w600">DELETE</a>' +
      '<a href="javascript:void(0);" class="text-success fs-14 font-w600">PUBLISH</a>' +
      "</div></div></div></div></div>"
    );
  }

  function wireSearch() {
    var input = qs(".search-area input.form-control");
    var btn = qs(".search-area .input-group-text, #rd-global-search-btn");
    if (!input || !btn) return;

    var panel = document.createElement("div");
    panel.id = "rd-search-panel";
    panel.style.cssText =
      "display:none;position:absolute;right:1rem;top:4.5rem;z-index:1050;min-width:320px;max-width:420px;background:#111;border:1px solid rgba(250,204,21,.25);padding:12px;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.45);color:#e8e8e8;";
    document.body.appendChild(panel);

    function runSearch() {
      var q = input.value || "";
      fetch("/api/search?format=html&q=" + encodeURIComponent(q))
        .then(function (r) {
          return r.text();
        })
        .then(function (html) {
          panel.style.display = "block";
          // Intentional sink for reflected XSS from /api/search?format=html
          panel.innerHTML = html;
        })
        .catch(function () {
          panel.style.display = "block";
          panel.textContent = "Search unavailable";
        });
    }

    btn.addEventListener("click", function (e) {
      e.preventDefault();
      runSearch();
    });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        runSearch();
      }
    });
  }

  function hydrateReviews() {
    var host = qs("#rd-live-reviews");
    var published = qs("#rd-live-reviews-published");
    if (!host && !published) return;
    fetch("/api/reviews")
      .then(function (r) {
        return r.json();
      })
      .then(function (data) {
        var rows = (data && data.reviews) || [];
        var html = rows
          .map(function (rev, idx) {
            return reviewCard(rev, idx);
          })
          .join("");
        if (!html) {
          html = '<div class="p-4 text-muted">No reviews yet.</div>';
        }
        if (host) host.innerHTML = html;
        if (published) published.innerHTML = html;
      })
      .catch(function () {
        if (host) host.innerHTML = '<div class="p-4 text-muted">Could not load reviews.</div>';
      });
  }

  function wireReviewComposer() {
    var form = qs("#rd-review-form");
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = (qs("[name=customer_name]", form) || {}).value || "Guest";
      var body = (qs("[name=body]", form) || {}).value || "";
      var rating = (qs("[name=rating]", form) || {}).value || "5";
      fetch("/api/reviews", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ customer_name: name, body: body, rating: rating }),
      })
        .then(function () {
          hydrateReviews();
          form.reset();
        })
        .catch(function () {});
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    wireSearch();
    hydrateReviews();
    wireReviewComposer();
  });
})();
