(function($) {
   /*  "use strict" */
   
 var dzSparkLine = function(){
    
	var screenWidth = $(window).width();
	
	function getSparkLineGraphBlockSize(selector)
	{
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
	
	var sparkLineDash = function(){
		// Line Chart
		if(jQuery('#sparklinedash').length > 0 ){	 
			$("#sparklinedash").sparkline([10, 15, 26, 27, 28, 31, 34, 40, 41, 44, 49, 64, 68, 69, 72], {
				type: "bar",
				height: "50",
				barWidth: "4",
				resize: !0,
				barSpacing: "5",
				barColor: "#FACC15",
			});
		}
	}
	
	var sparkLine8 = function(){
		if(jQuery('#sparkline8').length > 0 ){	
			$("#sparkline8").sparkline([79, 72, 29, 6, 52, 32, 73, 40, 14, 75, 77, 39, 9, 15, 10], {
				type: "line",
				//width: "100%",
				width: getSparkLineGraphBlockSize('#sparkline8'),
				height: "50",
				lineColor: "#FACC15",
				fillColor: "rgba(250, 204, 21, .5)",
				minSpotColor: "#FACC15",
				maxSpotColor: "#FACC15",
				highlightLineColor: "#FACC15",
				highlightSpotColor: "#FACC15",
				
			});
		}
	}
	
	var sparkLine9 = function(){
		if(jQuery('#sparkline9').length > 0 ){	
			$("#sparkline9").sparkline([27, 31, 35, 28, 45, 52, 24, 4, 50, 11, 54, 49, 72, 59, 75], {
				type: "line",
				//width: "100%",
				width: getSparkLineGraphBlockSize('#sparkline9'),
				height: "50",
				lineColor: "#ff5c00",
				fillColor: "rgba(255, 92, 0, .5)",
				minSpotColor: "#ff5c00",
				maxSpotColor: "#ff5c00",
				highlightLineColor: "rgb(255, 159, 0)",
				highlightSpotColor: "#ff5c00"
			});
		}
	}

    // Bar Chart
	var sparkBar = function(){
		if(jQuery('#spark-bar').length > 0 ){	
			$("#spark-bar").sparkline([33, 22, 68, 54, 8, 30, 74, 7, 36, 5, 41, 19, 43, 29, 38], {
				type: "bar",
				height: "200",
				barWidth: 6,
				barSpacing: 7,
				barColor: "#787878"
			});
		}	
	}
		
	var sparkBar2 = function(){
		if(jQuery('#spark-bar-2').length > 0 ){	
			$("#spark-bar-2").sparkline([33, 22, 68, 54, 8, 30, 74, 7, 36, 5, 41, 19, 43, 29, 38], {
				type: "bar",
				height: "140",
				width: 100,
				barWidth: 10,
				barSpacing: 10,
				barColor: "rgb(255, 206, 120)"
			});
		}	
	}
		
	var stackedBarChart = function(){
		if(jQuery('#StackedBarChart').length > 0 ){	
			$('#StackedBarChart').sparkline([
				[1, 4, 2],
				[2, 3, 2],
				[3, 2, 2],
				[4, 1, 2]
			], {
					type: "bar",
					height: "200",
					barWidth: 10,
					barSpacing: 7, 
					stackedBarColor: ['#FACC15', '#787878', '#ff5c00']
				});
		}
	}
		
	var triState = function(){
		if(jQuery('#tristate').length > 0 ){	

			$("#tristate").sparkline([1, 1, 0, 1, -1, -1, 1, -1, 0, 0, 1, 1], {
				type: 'tristate',
				height: "200",
				barWidth: 10,
				barSpacing: 7, 
				colorMap: ['#FACC15', '#787878', '#ff5c00'], 
				negBarColor: '#ff5c00'
			});
		}
	}
		
	var compositeBar = function(){
		// Composite
		if(jQuery('#composite-bar').length > 0 ){
			$("#composite-bar").sparkline([73, 53, 50, 67, 3, 56, 19, 59, 37, 32, 40, 26, 71, 19, 4, 53, 55, 31, 37], {
				type: "bar",
				height: "200",
				barWidth: "10",
				resize: true,
				// barSpacing: "7",
				barColor: "#FACC15", 
				width: '100%',
				
			});
		}	
	}	
	
	var sparklineCompositeChart = function(){
		if(jQuery('#sparkline-composite-chart').length > 0 ){
			$("#sparkline-composite-chart").sparkline([5, 6, 7, 2, 0, 3, 6, 8, 1, 2, 2, 0, 3, 6], {
				type: 'line',
				width: '100%',
				height: '200', 
				barColor: '#787878', 
				colorMap: ['#787878', '#ff5c00']
			});
		}
		if(jQuery('#sparkline-composite-chart').length > 0 ){
			$("#sparkline-composite-chart").sparkline([5, 6, 7, 2, 0, 3, 6, 8, 1, 2, 2, 0, 3, 6], {
				type: 'bar',
				height: '150px',
				width: '100%',
				barWidth: 10,
				barSpacing: 5,
				barColor: '#34C73B',
				negBarColor: '#34C73B',
				composite: true,
			});
		}
	}
		
	var sparkLine11 = function(){
		if(jQuery('#sparkline11').length > 0 ){
			//Pie
			$("#sparkline11").sparkline([24, 61, 51], {
				type: "pie",
				height: "100px",
				resize: !0,
				sliceColors: ["rgba(192, 10, 39, .5)", "rgba(0, 0, 128, .5)", "rgba(250, 204, 21, .5)"]
			});
		}	
	}	
	
	var sparkLine12 = function(){
		if(jQuery('#sparkline12').length > 0 ){
			//Pie
			$("#sparkline12").sparkline([24, 61, 51], {
				type: "pie",
				height: "100",
				resize: !0,
				sliceColors: ["rgba(179, 204, 255, 1)", "rgba(157, 189, 255, 1)", "rgba(112, 153, 237, 1)"]
			});
		}	
	}	
	
	var bulletChart = function(){
		if(jQuery('#bullet-chart').length > 0 ){
			// Bullet
			$("#bullet-chart").sparkline([10, 12, 12, 9, 7], {
				type: 'bullet',
				height: '100',
				width: '100%',
				targetOptions: { // Options related with look and position of targets 
					width: '100%',        // The width of the target 
					height: 3,            // The height of the target 
					borderWidth: 0,       // The border width of the target 
					borderColor: 'black', // The border color of the target 
					color: 'black'        // The color of the target 
				}
			});
		}
	}
		
	var boxPlot = function(){
		if(jQuery('#boxplot').length > 0 ){
			//Boxplot
			$("#boxplot").sparkline([4,27,34,52,54,59,61,68,78,82,85,87,91,93,100], {
				type: 'box'
			});
		}
	}
	
	
    /* Function ============ */
		return {
			init:function(){
			},
			
			
			load:function(){
				sparkLineDash();	
				sparkLine8();
				sparkLine9();	
				sparkBar();	
				sparkBar2();		
				stackedBarChart();
				triState();
				compositeBar();
				sparklineCompositeChart();
				bulletChart();
				sparkLine11();
				sparkLine12();
				boxPlot(); 
			},
			
			resize:function(){
				sparkLineDash();	
				sparkLine8();
				sparkLine9();	
				sparkBar();	
				sparkBar2();		
				stackedBarChart();
				triState();
				compositeBar();
				sparklineCompositeChart();
				bulletChart();
				sparkLine11();
				sparkLine12();
				boxPlot();
			}
		}
	
	}();

	jQuery(document).ready(function(){
	});
		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dzSparkLine.resize();	
		}, 1000);
	});

	jQuery(window).on('resize',function(){
		setTimeout(function(){
			dzSparkLine.resize();	
		}, 1000);
	});     

})(jQuery);