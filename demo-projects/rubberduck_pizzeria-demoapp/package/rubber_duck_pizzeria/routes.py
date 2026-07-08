from flask import Flask, render_template,Blueprint

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/index")
def index():
    context={
        "page_title":"Dashboard"
    }
    return render_template("rubber_duck_pizzeria/index.html",**context)

@main.route("/index-2")
def index_2():
    context={
        "page_title":"Dashboard Dark"
    }
    return render_template("rubber_duck_pizzeria/index-2.html",**context)
    
@main.route("/order-list")
def order_list():
    context={
        "page_title":"Order List"
    }
    return render_template("rubber_duck_pizzeria/order-list.html",**context)

@main.route("/order-detail")
def order_detail():
    context={
        "page_title":"Order Detail"
    }
    return render_template("rubber_duck_pizzeria/order-detail.html",**context)
    
@main.route("/customer-list")
def customer_list():
    context={
        "page_title":"Customer List"
    }
    return render_template("rubber_duck_pizzeria/customer-list.html",**context)
    
@main.route("/analytics")
def analytics():
    context={
        "page_title":"Analytics"
    }
    return render_template("rubber_duck_pizzeria/analytics.html",**context)

@main.route("/review")
def review():
    context={
        "page_title":"Review"
    }
    return render_template("rubber_duck_pizzeria/review.html",**context)

@main.route("/app-profile")
def app_profile():
    context={
        "page_title":"App Profile"
    }
    return render_template("rubber_duck_pizzeria/apps/app-profile.html",**context)

@main.route("/post-details")
def post_details():
    context={
        "page_title":"Post Details"
    }
    return render_template("rubber_duck_pizzeria/apps/post-details.html",**context)

@main.route("/email-compose")
def email_compose():
    context={
        "page_title":"Compose"
    }
    return render_template("rubber_duck_pizzeria/apps/email/email-compose.html",**context)

@main.route("/email-inbox")
def email_inbox():
    context={
        "page_title":"Inbox"
    }
    return render_template("rubber_duck_pizzeria/apps/email/email-inbox.html",**context)

@main.route("/email-read")
def email_read():
    context={
        "page_title":"Read"
    }
    return render_template("rubber_duck_pizzeria/apps/email/email-read.html",**context)

@main.route("/app-calendar")
def app_calendar():
    context={
        "page_title":"Calendar"
    }
    return render_template("rubber_duck_pizzeria/apps/app-calendar.html",**context)

@main.route("/ecom-product-grid")
def ecom_product_grid():
    context={
        "page_title":"Product Grid"
    }
    return render_template("rubber_duck_pizzeria/apps/shop/ecom-product-grid.html",**context)

@main.route("/ecom-product-list")
def ecom_product_list():
    context={
        "page_title":"Product List"
    }
    return render_template("rubber_duck_pizzeria/apps/shop/ecom-product-list.html",**context)

@main.route("/ecom-product-detail")
def ecom_product_detail():
    context={
        "page_title":"Product Detail"
    }
    return render_template("rubber_duck_pizzeria/apps/shop/ecom-product-detail.html",**context)

@main.route("/ecom-product-order")
def ecom_product_order():
    context={
        "page_title":"Product Order"
    }
    return render_template("rubber_duck_pizzeria/apps/shop/ecom-product-order.html",**context)

@main.route("/ecom-checkout")
def ecom_checkout():
    context={
        "page_title":"Checkout"
    }
    return render_template("rubber_duck_pizzeria/apps/shop/ecom-checkout.html",**context)

@main.route("/ecom-invoice")
def ecom_invoice():
    context={
        "page_title":"Invoice"
    }
    return render_template("rubber_duck_pizzeria/apps/shop/ecom-invoice.html",**context)

@main.route("/ecom-customers")
def ecom_customers():
    context={
        "page_title":"Customers"
    }
    return render_template("rubber_duck_pizzeria/apps/shop/ecom-customers.html",**context)

@main.route("/flat-icons")
def flat_icons():
    context={
        "page_title":"Flat Icons"
    }
    return render_template("rubber_duck_pizzeria/flat-icons.html",**context)

@main.route("/svg-icons")
def svg_icons():
    context={
        "page_title":"Svg Icons"
    }
    return render_template("rubber_duck_pizzeria/svg-icons.html",**context)

@main.route("/content")
def content():
    context={
        "page_title":"Content"
    }
    return render_template("rubber_duck_pizzeria/cms/content.html",**context)

@main.route("/add-content")
def add_content():
    context={
        "page_title":"Add Content"
    }
    return render_template("rubber_duck_pizzeria/cms/add-content.html",**context)

@main.route("/menu")
def menu():
    context={
        "page_title":"Menu"
    }
    return render_template("rubber_duck_pizzeria/cms/menu.html",**context)

@main.route("/email-template")
def email_template():
    context={
        "page_title":"Email Template"
    }
    return render_template("rubber_duck_pizzeria/cms/email-template.html",**context)

@main.route("/add-email")
def add_email():
    context={
        "page_title":"Add Email"
    }
    return render_template("rubber_duck_pizzeria/cms/add-email.html",**context)

@main.route("/blog")
def blog():
    context={
        "page_title":"Blog"
    }
    return render_template("rubber_duck_pizzeria/cms/blog.html",**context)

@main.route("/add-blog")
def add_blog():
    context={
        "page_title":"Add Blog"
    }
    return render_template("rubber_duck_pizzeria/cms/add-blog.html",**context)

@main.route("/blog-category")
def blog_category():
    context={
        "page_title":"Blog Category"
    }
    return render_template("rubber_duck_pizzeria/cms/blog-category.html",**context)

@main.route("/chart-flot")
def chart_flot():
    context={
        "page_title":"Chart Flot"
    }
    return render_template("rubber_duck_pizzeria/charts/chart-flot.html",**context)

@main.route("/chart-morris")
def chart_morris():
    context={
        "page_title":"Chart Morris"
    }
    return render_template("rubber_duck_pizzeria/charts/chart-morris.html",**context)

@main.route("/chart-chartjs")
def chart_chartjs():
    context={
        "page_title":"Chart Chartjs"
    }
    return render_template("rubber_duck_pizzeria/charts/chart-chartjs.html",**context)

@main.route("/chart-chartist")
def chart_chartist():
    context={
        "page_title":"Chart Chartist"
    }
    return render_template("rubber_duck_pizzeria/charts/chart-chartist.html",**context)

@main.route("/chart-sparkline")
def chart_sparkline():
    context={
        "page_title":"Chart Sparkline"
    }
    return render_template("rubber_duck_pizzeria/charts/chart-sparkline.html",**context)

@main.route("/chart-peity")
def chart_peity():
    context={
        "page_title":"Chart Peity"
    }
    return render_template("rubber_duck_pizzeria/charts/chart-peity.html",**context)


@main.route("/ui-accordion")
def ui_accordion():
    context={
        "page_title":"Accordion"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-accordion.html",**context)

@main.route("/ui-alert")
def ui_alert():
    context={
        "page_title":"Alert"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-alert.html",**context)

@main.route("/ui-badge")
def ui_badge():
    context={
        "page_title":"Badge"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-badge.html",**context)

@main.route("/ui-button")
def ui_button():
    context={
        "page_title":"Button"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-button.html",**context)

@main.route("/ui-modal")
def ui_modal():
    context={
        "page_title":"Modal"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-modal.html",**context)

@main.route("/ui-button-group")
def ui_button_group():
    context={
        "page_title":"Button Group"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-button-group.html",**context)

@main.route("/ui-list-group")
def ui_list_group():
    context={
        "page_title":"List Group"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-list-group.html",**context)

@main.route("/ui-media-object")
def ui_media_object():
    context={
        "page_title":"Media Object"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-media-object.html",**context)

@main.route("/ui-card")
def ui_card():
    context={
        "page_title":"Card"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-card.html",**context)

@main.route("/ui-carousel")
def ui_carousel():
    context={
        "page_title":"Carousel"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-carousel.html",**context)

@main.route("/ui-dropdown")
def ui_dropdown():
    context={
        "page_title":"Dropdown"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-dropdown.html",**context)

@main.route("/ui-popover")
def ui_popover():
    context={
        "page_title":"Popover"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-popover.html",**context)

@main.route("/ui-progressbar")
def ui_progressbar():
    context={
        "page_title":"Progressbar"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-progressbar.html",**context)

@main.route("/ui-tab")
def ui_tab():
    context={
        "page_title":"Tab"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-tab.html",**context)

@main.route("/ui-typography")
def ui_typography():
    context={
        "page_title":"Typography"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-typography.html",**context)

@main.route("/ui-pagination")
def ui_pagination():
    context={
        "page_title":"Pagination"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-pagination.html",**context)

@main.route("/ui-grid")
def ui_grid():
    context={
        "page_title":"Grid"
    }
    return render_template("rubber_duck_pizzeria/bootstrap/ui-grid.html",**context)

@main.route("/uc-select2")
def uc_select2():
    context={
        "page_title":"Select"
    }
    return render_template("rubber_duck_pizzeria/plugins/uc-select2.html",**context)

@main.route("/uc-nestable")
def uc_nestable():
    context={
        "page_title":"Nestable"
    }
    return render_template("rubber_duck_pizzeria/plugins/uc-nestable.html",**context)

@main.route("/uc-noui-slider")
def uc_noui_slider():
    context={
        "page_title":"UI Slider"
    }
    return render_template("rubber_duck_pizzeria/plugins/uc-noui-slider.html",**context)

@main.route("/uc-sweetalert")
def uc_sweetalert():
    context={
        "page_title":"Sweet Alert"
    }
    return render_template("rubber_duck_pizzeria/plugins/uc-sweetalert.html",**context)

@main.route("/uc-toastr")
def uc_toastr():
    context={
        "page_title":"Toastr"
    }
    return render_template("rubber_duck_pizzeria/plugins/uc-toastr.html",**context)

@main.route("/map-jqvmap")
def map_jqvmap():
    context={
        "page_title":"Jqvmap"
    }
    return render_template("rubber_duck_pizzeria/plugins/map-jqvmap.html",**context)

@main.route("/uc-lightgallery")
def uc_lightgallery():
    context={
        "page_title":"LightGallery"
    }
    return render_template("rubber_duck_pizzeria/plugins/uc-lightgallery.html",**context)

@main.route("/widget-basic")
def widget_basic():
    context={
        "page_title":"Widget"
    }
    return render_template("rubber_duck_pizzeria/widget-basic.html",**context)

@main.route("/form-element")
def form_element():
    context={
        "page_title":"Form Element"
    }
    return render_template("rubber_duck_pizzeria/forms/form-element.html",**context)

@main.route("/form-wizard")
def form_wizard():
    context={
        "page_title":"Form Wizard"
    }
    return render_template("rubber_duck_pizzeria/forms/form-wizard.html",**context)

@main.route("/form-editor")
def form_editor():
    context={
        "page_title":"CkEditor"
    }
    return render_template("rubber_duck_pizzeria/forms/form-editor.html",**context)

@main.route("/form-pickers")
def form_pickers():
    context={
        "page_title":"Pickers"
    }
    return render_template("rubber_duck_pizzeria/forms/form-pickers.html",**context)

@main.route("/form-validation")
def form_validation():
    context={
        "page_title":"Form Validation"
    }
    return render_template("rubber_duck_pizzeria/forms/form-validation.html",**context)

@main.route("/table-bootstrap-basic")
def table_bootstrap_basic():
    context={
        "page_title":"Table Bootstrap"
    }
    return render_template("rubber_duck_pizzeria/table/table-bootstrap-basic.html",**context)

@main.route("/table-datatable-basic")
def table_datatable_basic():
    context={
        "page_title":"Table Datatable"
    }
    return render_template("rubber_duck_pizzeria/table/table-datatable-basic.html",**context)


@main.route("/page-register")
def page_register():
    return render_template("rubber_duck_pizzeria/pages/page-register.html")

@main.route("/page-login")
def page_login():
    return render_template("rubber_duck_pizzeria/pages/page-login.html")

@main.route("/login")
def login():
    return render_template("rubber_duck_pizzeria/pages/login.html")

@main.route("/page-forgot-password")
def page_forgot_password():
    return render_template("rubber_duck_pizzeria/pages/page-forgot-password.html")

@main.route("/page-lock-screen")
def page_lock_screen():
    return render_template("rubber_duck_pizzeria/pages/page-lock-screen.html")

@main.route("/page-empty")
def page_empty():
    context={
        "page_title":"Empty Page"
    }
    return render_template("rubber_duck_pizzeria/pages/page-empty.html",**context)

@main.route("/page-error-400")
def page_error_400():
    return render_template("400.html")

@main.route("/page-error-403")    
def page_error_403():
    return render_template("403.html")

@main.route("/page-error-404")
def page_error_404():
    return render_template("404.html")

@main.route("/page-error-500")
def page_error_500():
    return render_template("500.html")

@main.route("/page-error-503")
def page_error_503():
    return render_template("503.html")



