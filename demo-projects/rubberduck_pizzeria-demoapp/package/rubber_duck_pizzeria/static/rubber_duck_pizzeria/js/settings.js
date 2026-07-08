var body = $('body');
var html = $('html');

function dezSettings({typography, version, layout, navheaderBg, headerBg, sidebarStyle, sidebarBg, sidebarPosition, headerPosition, containerLayout, direction, primary}) {
    this.typography = typography || "poppins";
    this.version = version || "light";
    this.layout = layout || "vertical";
    this.navheaderBg = navheaderBg || "color_1";
    this.headerBg = headerBg || "color_1";
    this.sidebarStyle = sidebarStyle || "full";
    this.sidebarBg = sidebarBg || "color_1";
    this.sidebarPosition = sidebarPosition || "static";
    this.headerPosition = headerPosition || "static";
    this.containerLayout = containerLayout || "wide";
    this.direction = direction || "ltr";
	this.primary = primary || "color_1";

    this.manageTypography();
    this.manageVersion();
    this.manageLayout();
    this.manageNavHeaderBg();
    this.manageHeaderBg();
    this.manageSidebarStyle();
    this.manageSidebarBg();
    this.manageSidebarPosition();
    this.manageHeaderPosition();
    this.manageContainerLayout();
    this.manageRtlLayout();
    this.manageResponsiveSidebar();
	this.managePrimaryColor();
}
dezSettings.prototype.manageVersion = function() {
    switch(this.version) {
        case "light": 
            body.attr("data-theme-version", "light");
            break;
        case "dark": 
            body.attr("data-theme-version", "dark");
            break;
        case "transparent": 
            body.attr("data-theme-version", "transparent");
            break;
        default: 
            body.attr("data-theme-version", "light");
    }
}
dezSettings.prototype.manageTypography = function() {
    switch(this.typography) {
        case "poppins": 
            body.attr("data-typography", "poppins");
            break;
        case "roboto": 
            body.attr("data-typography", "roboto");
            break;
        case "opensans": 
            body.attr("data-typography", "opensans");
            break;
		case "helveticaneue": 
            body.attr("data-typography", "helveticaneue");
            break;
        default: 
            body.attr("data-typography", "poppins");
    }
}
dezSettings.prototype.manageLayout = function() {
    switch(this.layout) {
        case "horizontal": 
            this.sidebarStyle === "overlay" ? body.attr("data-sidebar-style", "full") : body.attr("data-sidebar-style", `${this.sidebarStyle}`);
            body.attr("data-layout", "horizontal");
            break;
        case "vertical": 
            body.attr("data-layout", "vertical");
            break;
        default:
            body.attr("data-layout", "vertical");
    }
}
dezSettings.prototype.manageNavHeaderBg = function() {
    switch(this.navheaderBg) {
        case "color_1": 
            body.attr("data-nav-headerbg", "color_1");
            break;
        case "color_2": 
            body.attr("data-nav-headerbg", "color_2");
            break;
        case "color_3": 
            body.attr("data-nav-headerbg", "color_3");
            break;
        case "color_4": 
            body.attr("data-nav-headerbg", "color_4");
            break;
        case "color_5": 
            body.attr("data-nav-headerbg", "color_5");
            break;
        case "color_6": 
            body.attr("data-nav-headerbg", "color_6");
            break;
        case "color_7": 
            body.attr("data-nav-headerbg", "color_7");
            break;
        case "color_8": 
            body.attr("data-nav-headerbg", "color_8");
            break;
        case "color_9": 
            body.attr("data-nav-headerbg", "color_9");
            break;
        case "color_10": 
            body.attr("data-nav-headerbg", "color_10");
            break;
		case "color_11": 
            body.attr("data-nav-headerbg", "color_11");
            break;
		case "color_12": 
            body.attr("data-nav-headerbg", "color_12");
            break;
		case "color_13": 
            body.attr("data-nav-headerbg", "color_13");
            break;
		case "color_14": 
            body.attr("data-nav-headerbg", "color_14");
            break;
		case "color_15": 
            body.attr("data-nav-headerbg", "color_15");
            break;		
        case "image_1": 
            body.attr("data-nav-headerbg", "image_1");
            break;
        case "image_2": 
            body.attr("data-nav-headerbg", "image_2");
            break;
        case "image_3": 
            body.attr("data-nav-headerbg", "image_3");
            break;
        default:
            body.attr("data-nav-headerbg", "color_1");
    }
}
dezSettings.prototype.manageHeaderBg = function() {
    switch(this.headerBg) {
        case "color_1": 
            body.attr("data-headerbg", "color_1");
            break;
        case "color_2": 
            body.attr("data-headerbg", "color_2");
            break;
        case "color_3": 
            body.attr("data-headerbg", "color_3");
            break;
        case "color_4": 
            body.attr("data-headerbg", "color_4");
            break;
        case "color_5": 
            body.attr("data-headerbg", "color_5");
            break;
        case "color_6": 
            body.attr("data-headerbg", "color_6");
            break;
        case "color_7": 
            body.attr("data-headerbg", "color_7");
            break;
        case "color_8": 
            body.attr("data-headerbg", "color_8");
            break;
        case "color_9": 
            body.attr("data-headerbg", "color_9");
            break;
        case "color_10": 
            body.attr("data-headerbg", "color_10");
            break;
		case "color_11": 
            body.attr("data-headerbg", "color_11");
            break;
		case "color_12": 
            body.attr("data-headerbg", "color_12");
            break;
		case "color_13": 
            body.attr("data-headerbg", "color_13");
            break;
		case "color_14": 
            body.attr("data-headerbg", "color_14");
            break;
		case "color_15": 
            body.attr("data-headerbg", "color_15");
            break;		
        case "transparent": 
            body.attr("data-headerbg", "transparent");
            break;
        case "gradient_1": 
            body.attr("data-headerbg", "gradient_1");
            break;
        case "gradient_2": 
            body.attr("data-headerbg", "gradient_2");
            break;
        case "gradient_3": 
            body.attr("data-headerbg", "gradient_3");
            break;
        default:
            body.attr("data-headerbg", "color_1");
    }
}
dezSettings.prototype.manageSidebarStyle = function() {
	switch(this.sidebarStyle) {
        case "full":
            body.attr("data-sidebar-style", "full");
            break;
        case "mini":
            body.attr("data-sidebar-style", "mini");
            break;
        case "compact":
            body.attr("data-sidebar-style", "compact");
            break;
        case "modern":
            body.attr("data-sidebar-style", "modern");
            break;
        case "icon-hover":
            body.attr("data-sidebar-style", "icon-hover");
			break;
        case "overlay":
            this.layout === "horizontal" ? body.attr("data-sidebar-style", "full") : body.attr("data-sidebar-style", "overlay");
            break;
        default:
            body.attr("data-sidebar-style", "full");
    }
}
dezSettings.prototype.manageSidebarBg = function() {
    switch(this.sidebarBg) {
        case "color_1": 
            body.attr("data-sibebarbg", "color_1");
            break;
        case "color_2": 
            body.attr("data-sibebarbg", "color_2");
            break;
        case "color_3": 
            body.attr("data-sibebarbg", "color_3");
            break;
        case "color_4": 
            body.attr("data-sibebarbg", "color_4");
            break;
        case "color_5": 
            body.attr("data-sibebarbg", "color_5");
            break;
        case "color_6": 
            body.attr("data-sibebarbg", "color_6");
            break;
        case "color_7": 
            body.attr("data-sibebarbg", "color_7");
            break;
        case "color_8": 
            body.attr("data-sibebarbg", "color_8");
            break;
        case "color_9": 
            body.attr("data-sibebarbg", "color_9");
            break;
        case "color_10": 
            body.attr("data-sibebarbg", "color_10");
            break;
		case "color_11": 
            body.attr("data-sibebarbg", "color_11");
            break;
		case "color_12": 
            body.attr("data-sibebarbg", "color_12");
            break;
		case "color_13": 
            body.attr("data-sibebarbg", "color_13");
            break;
		case "color_14": 
            body.attr("data-sibebarbg", "color_14");
            break;
		case "color_15": 
            body.attr("data-sibebarbg", "color_15");
            break;			
        case "image_1": 
            body.attr("data-sibebarbg", "image_1");
            break;
        case "image_2": 
            body.attr("data-sibebarbg", "image_2");
            break;
        case "image_3": 
            body.attr("data-sibebarbg", "image_3");
            break;
        default:
            body.attr("data-sibebarbg", "color_1");
    }
}
dezSettings.prototype.manageSidebarPosition = function() {
    switch(this.sidebarPosition) {
        case "fixed": 
            this.sidebarStyle === "overlay" && this.layout === "vertical" || this.sidebarStyle === "modern" ? body.attr("data-sidebar-position", "static") : body.attr("data-sidebar-position", "fixed");
            break;
        case "static": 
            body.attr("data-sidebar-position", "static");
            break;
        default: 
            body.attr("data-sidebar-position", "fixed");       
    }
}
dezSettings.prototype.manageHeaderPosition = function() {
    switch(this.headerPosition) {
        case "fixed": 
            body.attr("data-header-position", "fixed");
            break;
        case "static": 
            body.attr("data-header-position", "static");
            break;
        default: 
            body.attr("data-header-position", "fixed");       
    }
}
dezSettings.prototype.manageContainerLayout = function() {
    switch(this.containerLayout) {
        case "boxed":
            if(this.layout === "vertical" && this.sidebarStyle === "full") {
                body.attr("data-sidebar-style", "overlay");
            }
            body.attr("data-container", "boxed");
            break;
        case "wide":
            body.attr("data-container", "wide");
            break;
        case "wide-boxed": 
            body.attr("data-container", "wide-boxed");
            break;
        default:
            body.attr("data-container", "wide");
    }
}
dezSettings.prototype.manageRtlLayout = function() {
	switch(this.direction) {
        case "rtl":
            html.attr("dir", "rtl");
            html.addClass('rtl');
            body.attr("direction", "rtl");
            break;
        case "ltr": 
            html.attr("dir", "ltr");
            html.removeClass('rtl');
            body.attr("direction", "ltr");
            break;
        default: 
            html.attr("dir", "ltr");
            body.attr("direction", "ltr");
    }
}
dezSettings.prototype.manageResponsiveSidebar = function() {
    const innerWidth = $(window).innerWidth();
    if(innerWidth < 1024) {
        body.attr("data-layout", "vertical");
        body.attr("data-container", "wide");
    }

    if(innerWidth > 767 && innerWidth < 1024) {
        body.attr("data-sidebar-style", "mini");
    }

    if(innerWidth < 768) {
        body.attr("data-sidebar-style", "overlay");
    }
}
dezSettings.prototype.managePrimaryColor = function() {
	switch(this.primary) {
        case "color_1": 
            body.attr("data-primary", "color_1");
			 break;
        case "color_2": 
            body.attr("data-primary", "color_2");
            break;
		case "color_3": 
            body.attr("data-primary", "color_3");
            break;
		case "color_4": 
            body.attr("data-primary", "color_4");
            break;
		case "color_5": 
            body.attr("data-primary", "color_5");
            break;
		case "color_6": 
            body.attr("data-primary", "color_6");
            break;	
		case "color_7": 
            body.attr("data-primary", "color_7");
            break;
		case "color_8": 
            body.attr("data-primary", "color_8");
            break;
		case "color_9": 
            body.attr("data-primary", "color_9");
            break;
		case "color_10": 
            body.attr("data-primary", "color_10");
            break;
		case "color_11": 
            body.attr("data-primary", "color_11");
            break;
		case "color_12": 
            body.attr("data-primary", "color_12");
            break;
		case "color_13": 
            body.attr("data-primary", "color_13");
            break;
		case "color_14": 
            body.attr("data-primary", "color_14");
            break;
		case "color_15": 
            body.attr("data-primary", "color_15");
            break;	
			
        default:
            body.attr("data-primary", "color_1");
    }
}