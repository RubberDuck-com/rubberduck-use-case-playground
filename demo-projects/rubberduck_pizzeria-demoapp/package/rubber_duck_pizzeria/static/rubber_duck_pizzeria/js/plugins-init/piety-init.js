
(function($) {
    "use strict"


/****************
Piety chart
*****************/
var dzPiety = function(){
	
	var getGraphBlockSize = function (selector) {
		var screenWidth = $(window).width();
		var graphBlockSize = '100%';
		
		if(screenWidth <= 768)
			{
				screenWidth = (screenWidth < 300 )?screenWidth:300;
				
				var blockWidth  = jQuery(selector).parent().innerWidth() - jQuery(selector).parent().width();
		
				blockWidth = Math.abs(blockWidth);
				
				var graphBlockSize = screenWidth - blockWidth - 10;	
			}		
		
		return graphBlockSize;
		
	}
	
	var handlePietyBarLine = function(){
		if(jQuery('.bar-line').length > 0 ){
			$(".bar-line").peity("bar", {
				width: "100",
				height: "100"
			});
		}
	}

    var handlePietyPie = function(){
		if(jQuery('span.pie').length > 0 ){
			$("span.pie").peity("pie", {
				fill: ['#FACC15', 'rgba(250, 204, 21, .3)'], 
				width: "100",
				height: "100"
			});
		}
	}
    
    var handlePietyDonut = function(){
		if(jQuery('span.donut').length > 0 ){
			$("span.donut").peity("donut", {
				width: "100",
				height: "100"
			});
		}
	}
    
	var handlePietyLine = function(){
		if(jQuery('.peity-line').length > 0 ){
			$(".peity-line").peity("line", {
				fill: ["rgba(250, 204, 21, .5)"], 
				stroke: '#FACC15', 
				width: "100%",
				height: "100"
			});
		}
	}
    
	var handlePietyLine2 = function(){
		if(jQuery('.peity-line-2').length > 0 ){
			$(".peity-line-2").peity("line", {
				fill: "#fa707e", 
				stroke: "#f77f8b", 
				//width: "100%",
				width: getGraphBlockSize('.peity-line-2'),
				strokeWidth: "3",
				height: "150"
			});
		}
	}
	
	var handlePietyLine3 = function(){
		if(jQuery('.peity-line-3').length > 0 ){
			$(".peity-line-3").peity("line", {
				fill: "#673bb7", 
				stroke: "#ab84f3", 
				width: "100%",
				strokeWidth: "3",
				height: "150"
			});
		}
	}
	
	var handlePietyBar = function(){
		if(jQuery('.bar').length > 0 ){
			$(".bar").peity("bar", {
				fill: ["#FACC15", "#787878", "#3693FF"],  
				width: "100%",
				height: "100",
			});
		}
	}
	
	var handlePietyBar1 = function(){
		if(jQuery('.bar1').length > 0 ){
			$(".bar1").peity("bar", {
				fill: ["#FACC15", "#787878", "#3693FF"],    
				//width: "100%",
				width: getGraphBlockSize('.bar1'),
				height: "140"
			});
		}
	}
	
	var handlePietyBarColours1 = function(){
		if(jQuery('.bar-colours-1').length > 0 ){
			$(".bar-colours-1").peity("bar", {
				fill: ["#FACC15", "#787878", "#3693FF"],  
				width: "100",
				height: "100"
			});
		}
	}
	
	var handlePietyBarColours2 = function(){
		if(jQuery('.bar-colours-2').length > 0 ){
			$(".bar-colours-2").peity("bar", {
				fill: function(t, e, i) {
					return "rgb(58, " + parseInt(e / i.length * 122) + ", 254)"
				},
				width: "100",
				height: "100"
			});
		}
	}
	
	var handlePietyBarColours3 = function(){
		if(jQuery('.bar-colours-3').length > 0 ){
			$(".bar-colours-3").peity("bar", {
				fill: function(t, e, i) {
					return "rgb(16, " + parseInt(e / i.length * 202) + ", 147)"
				},
				width: "100",
				height: "100"
			});
		}
	}
    
	var handlePietyColours1 = function(){
		if(jQuery('.pie-colours-1').length > 0 ){
			$(".pie-colours-1").peity("pie", {
				fill: ["cyan", "magenta", "yellow", "black"],
				width: "100",
				height: "100"
			});
		}
	}
	
    var handlePietyColours2 = function(){
		if(jQuery('.pie-colours-2').length > 0 ){
			$(".pie-colours-2").peity("pie", {
				fill: ["#FACC15", "#787878", "#3693FF", "#ff5c00", "#EE3C3C"],
				width: "100",
				height: "100"
			});
		}
	}
    
    var handlePietyDataAttr = function(){
		if(jQuery('.data-attr').length > 0 ){
			$(".data-attr").peity("donut");
		}
	}
    
    var handlePietyUpdatingChart = function(){
		var t = $(".updating-chart").peity("line", {
			fill: ['rgba(250, 204, 21, .5)'],
			stroke: 'rgb(250, 204, 21)', 
			width: "100%",
			height: 100
		});
		
		 setInterval(function() {
			var e = Math.round(10 * Math.random()),
			i = t.text().split(",");
			i.shift(), i.push(e), t.text(i.join(",")).change()
		}, 1e3);
	}
    
	/* Function ============ */
	return {
		init:function(){
		},
		
		
		load:function(){
			handlePietyBarLine();
			handlePietyPie();
			handlePietyDonut();
			handlePietyLine();
			handlePietyLine2();
			handlePietyLine3();
			handlePietyBar();
			handlePietyBar1();
			handlePietyBarColours1();
			handlePietyBarColours2();
			handlePietyBarColours3();
			handlePietyColours1();
			handlePietyColours2();
			handlePietyDataAttr();
			handlePietyUpdatingChart();
		},
		
		resize:function(){
			
		}
	}
	
}();
 
	jQuery(document).ready(function(){
		
		
		
	});
		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dzPiety.load();
		}, 1000); 
		
	});

	jQuery(window).on('resize',function(){
		setTimeout(function(){
			dzPiety.resize();
		}, 1000); 
		
	});      

})(jQuery);