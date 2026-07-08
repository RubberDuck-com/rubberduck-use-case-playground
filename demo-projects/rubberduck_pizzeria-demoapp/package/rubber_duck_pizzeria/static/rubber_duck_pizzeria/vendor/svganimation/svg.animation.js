(function(){
	
	
	$(window).on('load',function(){

		var settings = $.extend({
		        type: 'oneByOne',
		        start: 'inViewport',
		        dashGap: 10,
		        duration: 100
		    }, 'body' );
			
		$('svg' ).each(function() {
				var iconID = $(this).attr('id');
				if(iconID != undefined){
					var iconVar = iconID.replace( '-', '' );
					window['tc'+iconVar] = new Vivus( iconID, settings );
				}
				
		});

		$(document).delegate( ".ai-icon", "mouseenter", function() {
			var iconID = $(this).find('svg').attr('id');
			if(!iconID) return false;
			var iconVar = iconID.replace( '-', '' );
			window['tc'+iconVar].reset().play();
		});
		
	});
})();