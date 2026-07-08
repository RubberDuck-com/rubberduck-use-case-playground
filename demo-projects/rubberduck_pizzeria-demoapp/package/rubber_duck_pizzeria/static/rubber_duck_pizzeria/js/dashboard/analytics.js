(function($) {
    /* "use strict" */
	
 var dzChartlist = function(){
	
	var screenWidth = $(window).width();	
	var chartTimeline = function(){
		
		var optionsTimeline = {
			chart: {
				type: "bar",
				height: 370,
				stacked: true,
				toolbar: {
					show: false
				},
			},
			series: [
				 {
					name: "New Clients",
					data: [300, 450, 600, 600, 400, 450, 410, 470, 480, 800, 600, 900, 400]
				}
			],
			
			plotOptions: {
				bar: {
					columnWidth: "20%",
					
					colors: {
						backgroundBarColors: ['#2a2a2a', '#2a2a2a', '#2a2a2a', '#2a2a2a','#2a2a2a','#2a2a2a','#2a2a2a','#2a2a2a'],
						backgroundBarOpacity: 1,
						backgroundBarRadius: 5,
					},

				},
				distributed: true
			},
			colors:['#FFD54F'],
			grid: {
				show: false,
			},
			legend: {
				show: false
			},
			fill: {
			  opacity: 1
			},
			dataLabels: {
				enabled: false,
				colors: ['#000'],
				dropShadow: {
				  enabled: true,
				  top: 1,
				  left: 1,
				  blur: 1,
				  bottom:0,
				  opacity: 1
			  }
			},
			xaxis: {
			 categories: ['06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
			  labels: {
			   style: {
				  colors: '#787878',
				  fontSize: '14px',
				  fontFamily: 'poppins',
				  fontWeight: 400,
				  cssClass: 'apexcharts-xaxis-label',
				},
			  },
			  crosshairs: {
				show: false,
			  },
			  axisBorder: {
				  show: false,
				},
			},
			yaxis: {
			show:true,	
			labels: {
				offsetX: -15,
			   style: {
				  colors: '#7E7F80',
				  fontSize: '14px',
				   fontFamily: 'Poppins',
				  fontWeight: 100,
				  
				},
				 formatter: function (y) {
						  return y.toFixed(0) + "k";
						}
			  },
			},
			tooltip: {
				x: {
					show: true
				}
			},
			 responsive: [{
				breakpoint: 575,
				options: {
					chart: {
						height: 250,
					}
				}
			 }]
		};
		var chartTimelineRender =  new ApexCharts(document.querySelector("#chartTimeline"), optionsTimeline);
		 chartTimelineRender.render();
	}
	var donutChart = function(){
		$("span.donut").peity("donut", {
			width: "70",
			height: "70"
		});
	}
	
	 var revenueMap = function(){
		  var options = {
			  series: [
				{
					name: 'Net Profit',
					data: [500, 500, 200, 200, 600, 600, 1000, 1000,300, 300,500,500],
					//radius: 12,	
				}, 				
			],
				chart: {
				type: 'area',
				height: 350,
				toolbar: {
					show: false,
				},
				
			},
			plotOptions: {
			  bar: {
				horizontal: false,
				columnWidth: '55%',
				endingShape: 'rounded'
			  },
			},
			colors:['#FFD54F'],
			dataLabels: {
			  enabled: false,
			},
			markers: {
				shape: "circle",
			},
	
			legend: {
				show: false,
			},
			stroke: {
			  show: true,
			  width: 4,
			  curve:'straight',
			  colors:['#FFD54F'],
			},
			
			grid: {
				borderColor: 'rgba(255,255,255,0.08)',
			},
			xaxis: {
				
			  categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov','Dec'],
			  labels: {
				style: {
					colors: '#7E7F80',
					fontSize: '13px',
					fontFamily: 'Poppins',
					fontWeight: 100,
					cssClass: 'apexcharts-xaxis-label',
				},
			  },
			  crosshairs: {
			  show: false,
			  }
			},
			yaxis: {
			show:true,	
			labels: {
				offsetX: -15,
			   style: {
				  colors: '#7E7F80',
				  fontSize: '14px',
				   fontFamily: 'Poppins',
				  fontWeight: 100,
				  
				},
				 formatter: function (y) {
						  return y.toFixed(0) + "k";
						}
			  },
			},
			fill: {
			  opacity: 0.28,
			  colors:['#FFD54F']
			},
			tooltip: {
			  y: {
				formatter: function (val) {
				  return "$ " + val + " thousands"
				}
			  }
			}
			};

			var chartBar1 = new ApexCharts(document.querySelector("#revenueMap"), options);
			chartBar1.render();
		 
		 
	 }
	
	var customerMapkm = function(){
        var options = {
          series: [{
          name: 'Income',
          data: [80, 24, 80, 90]
        }, {
          name: 'Expense',
          data: [40, 60, 20, 60]
        }, {
          name: 'Others',
          data: [20, 17, 5, 20]
        }],
          chart: {
          type: 'bar',
          height: 350,
		  toolbar:{
			show:false
		  }
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '60%',
            endingShape: 'rounded'
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
			show: true,
          width: 3,
          colors: ['transparent']
        },
		legend: {
			show: false,
			fontSize: '12px',
			 markers: {
			  width: 20,
			  height: 20
			},
			itemMargin: {
				  horizontal: 10,
				  vertical: 10
			  },
		},
        xaxis: {
          categories: [ 'Week1','Week2', 'Week3', 'Week4'],
		  labels: {
				style: {
					colors: '#787878',
					fontSize: '13px',
					fontFamily: 'Poppins',
					fontWeight: 400
					
				},
			}
        },
        yaxis: {
			labels: {
				offsetX: -15,
					style: {
						colors: '#787878',
						fontSize: '13px',
						fontFamily: 'Poppins',
						fontWeight: 400
						
					},
				}
        },
		colors:['#FFD54F','#787878','#C4C4C4'],
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "$ " + val + " thousands"
            }
          }
        }
        };

        var chart = new ApexCharts(document.querySelector("#customerMapkm"), options);
        chart.render();
		
	}
	/* Function ============ */
		return {
			init:function(){
			},
			
			
			load:function(){
					chartTimeline();
					donutChart();
					revenueMap();
					customerMapkm();
					
			},
			
			resize:function(){
			}
		}
	
	}();

	jQuery(document).ready(function(){
	});
		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dzChartlist.load();
		}, 1000); 
		
	});

	jQuery(window).on('resize',function(){
		
		
	});     

})(jQuery);