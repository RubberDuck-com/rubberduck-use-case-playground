"use strict"

var dezSettingsOptions = {};

function getUrlParams(dParam){
	var dPageURL = window.location.search.substring(1),
		dURLVariables = dPageURL.split('&'),
		dParameterName,
		i;

	for (i = 0; i < dURLVariables.length; i++) {
		dParameterName = dURLVariables[i].split('=');

		if (dParameterName[0] === dParam) {
			return dParameterName[1] === undefined ? true : decodeURIComponent(dParameterName[1]);
		}
	}
}
/* Cookies Function */
function setCookie(cname, cvalue, exhours){
	var d = new Date();
	d.setTime(d.getTime() + (30*60*1000)); /* 30 Minutes */
	var expires = "expires="+ d.toString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname){
	var name = cname + "=";
	var decodedCookie = decodeURIComponent(document.cookie);
	var ca = decodedCookie.split(';');
	for(var i = 0; i <ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}
function deleteCookie(cname){
	var d = new Date();
	d.setTime(d.getTime() + (1)); // 1/1000 second
	var expires = "expires="+ d.toString();
	document.cookie = cname + "=1;" + expires + ";path=/";
}
function deleteAllCookie(reload = true){
	jQuery.each(themeOptionArr, function(optionKey, optionValue) {
		deleteCookie(optionKey);
	});
	if(reload){
		location.reload();
	}
}

/* Cookies Function END */
(function($) {
	
	"use strict"
	
	var body = $('body');
	var direction =  getUrlParams('dir');
	
	dezSettingsOptions = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: 'ltr'
	};
	
	new dezSettings(dezSettingsOptions);

	jQuery(window).on('resize',function(){
        /*Check container layout on resize */
        dezSettingsOptions.containerLayout = $('#container_layout').val();
        /*Check container layout on resize END */
        
		new dezSettings(dezSettingsOptions); 
	});

	if(direction == 'rtl' || body.attr('direction') == 'rtl'){
        direction = 'rtl';
		jQuery('.main-css').attr('href','/static/rubber_duck_pizzeria/css/style-rtl.css');
    }else{
        direction = 'ltr';
		jQuery('.main-css').attr('href','/static/rubber_duck_pizzeria/css/style.css');
	}
	
})(jQuery);