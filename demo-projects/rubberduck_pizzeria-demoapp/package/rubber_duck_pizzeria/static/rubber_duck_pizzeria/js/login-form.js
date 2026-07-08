var DZFormValidate = function(){
	
	var loginForm = function(){
		
		jQuery("#dz_login_signup_form").validate({
				rules: {
					"val-username": {
						required: !0,
						minlength: 3
					},
					"val-email": {
						required: !0,
						email: !0
					},
					"val-password": {
						required: !0,
						minlength: 5
					}
				},
				messages: {
					"val-username": {
						required: "Please enter a username",
						minlength: "Your username must consist of at least 3 characters"
					},
					"val-email": "Please enter a valid email address",
					"val-password": {
						required: "Please provide a password",
						minlength: "Your password must be at least 5 characters long"
					}
				},

				ignore: [],
				errorClass: "invalid-feedback animated fadeInUp",
				errorElement: "div",
				errorPlacement: function(e, a) {
					jQuery(a).parents(".form-group > div").append(e)
				},
				highlight: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid").addClass("is-invalid");
				},
				success: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid"), jQuery(e).remove()
				},
				invalidHandler: function(event, validator) {
					sweetAlert("Oops...", "Something went wrong !!", "error")
				},
				submitHandler: function(form) {
					sweetAlert("Good...", "Success !!", "success")
					return false;
				}
			});

		
		jQuery("#dz_login_signin_form").validate({
				rules: {
					
					"val-email": {
						required: !0,
						email: !0
					},
					"val-password": {
						required: !0,
						minlength: 5
					}
				},
				messages: {
					
					"val-email": "Please enter a valid email address",
					"val-password": {
						required: "Please provide a password",
						minlength: "Your password must be at least 5 characters long"
					}
				},

				ignore: [],
				errorClass: "invalid-feedback animated fadeInUp",
				errorElement: "div",
				errorPlacement: function(e, a) {
					jQuery(a).parents(".form-group > div").append(e)
				},
				highlight: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid").addClass("is-invalid");
				},
				success: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid"), jQuery(e).remove()
				},
				invalidHandler: function(event, validator) {
					sweetAlert("Oops...", "Something went wrong !!", "error")
				},
				submitHandler: function(form) {
					sweetAlert("Good...", "Success !!", "success")
					return false;
				}
			});
		
		jQuery("#dz_login_forgot_form").validate({
				rules: {
					"val-password": {
						required: !0,
						minlength: 5
					}
				},
				messages: {
					"val-password": {
						required: "Please provide a password",
						minlength: "Your password must be at least 5 characters long"
					}
				},

				ignore: [],
				errorClass: "invalid-feedback animated fadeInUp",
				errorElement: "div",
				errorPlacement: function(e, a) {
					jQuery(a).parents(".form-group > div").append(e)
				},
				highlight: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid").addClass("is-invalid");
				},
				success: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid"), jQuery(e).remove()
				},
				invalidHandler: function(event, validator) {
					sweetAlert("Oops...", "Something went wrong !!", "error")
				},
				submitHandler: function(form) {
					sweetAlert("Good...", "Success !!", "success")
					return false;
				}
			});
		
	}
	
	

	
	var formWithIcon = function(){
		
		jQuery(".form-valide-with-icon").validate({
				rules: {
					"val-username": {
						required: !0,
						minlength: 3
					},
					"val-password": {
						required: !0,
						minlength: 5
					}
				},
				messages: {
					"val-username": {
						required: "Please enter a username",
						minlength: "Your username must consist of at least 3 characters"
					},
					"val-password": {
						required: "Please provide a password",
						minlength: "Your password must be at least 5 characters long"
					}
				},

				ignore: [],
				errorClass: "invalid-feedback animated fadeInUp",
				errorElement: "div",
				errorPlacement: function(e, a) {
					jQuery(a).parents(".form-group > div").after(e);
					
				},
				highlight: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid").addClass("is-invalid");
					
				},
				success: function(e) {
					jQuery(e).closest(".form-group").removeClass("is-invalid").addClass("is-valid")
					
				},
				
		});
	}
	
	// Public Functions
    return {
        // public functions
        init: function() {
			loginForm();
			formWithIcon();
        }
    };
}();


// Initialization
jQuery(document).ready(function() {
    DZFormValidate.init();
});


