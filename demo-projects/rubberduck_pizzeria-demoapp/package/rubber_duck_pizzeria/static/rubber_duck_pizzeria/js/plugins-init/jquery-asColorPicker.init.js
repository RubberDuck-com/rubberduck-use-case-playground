(function($) {
    "use strict"
    
    // Colorpicker
    $(".as_colorpicker").asColorPicker();
    $(".complex-colorpicker").asColorPicker({
        mode: 'complex'
    });
    
	$(".gradient-colorpicker").asColorPicker({
    mode: 'gradient',
    gradient: {
        switchable: false
    }
});
})(jQuery);