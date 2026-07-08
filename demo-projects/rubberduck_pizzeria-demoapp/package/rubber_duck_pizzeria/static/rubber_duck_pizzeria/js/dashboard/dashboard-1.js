(function($) {
    /* "use strict" */
	
 var dzChartlist = function(){
	
	var screenWidth = $(window).width();	
	
	var radialChart = function(){
		 var options = {
          series: [70],
          chart: {
          height: 230,
          type: 'radialBar',
          toolbar: {
            show: false
          }
        },
        plotOptions: {
          radialBar: {
			hollow: {
              margin: 20,
              size: '65%',
              background: '#141414',
              image: undefined,
              imageOffsetX: 0,
              imageOffsetY: 0,
              position: 'front',
              dropShadow: {
                enabled: true,
                top: 3,
                left: 0,
                blur: 10,
                opacity: 0.1
              }
            },
            track: {
              background: '#2a2a2a',
              strokeWidth: '100%',
              margin: 0, // margin is in pixels
            },
        
            dataLabels: {
              show: true,
              value: {
				offsetY:-7,
                color: '#e8e8e8',
                fontSize: '20px',
                show: true,
              }
            }
          }
        },
        fill: {
            colors: ['#FFD54F'],
        },
        stroke: {
        },
        labels: [''],
        };

        var chart = new ApexCharts(document.querySelector("#radialChart"), options);
        chart.render();
	}
	var customerMap = function(){
         var options = {
          series: [{
          name: 'Income',
          data: [80, 24, 80, 90, 80, 70, 20, 85, 80, 45, 25, 65]
        }, {
          name: 'Expense',
          data: [40, 60, 20, 60, 60, 20, 60, 25, 40, 65, 15, 40]
        }, {
          name: 'Others',
          data: [20, 17, 5, 20, 20, 10, 15, 10, 15, 20, 60, 15]
        }],
          chart: {
          type: 'bar',
          height: 400,
		  toolbar:{
			show:false
		  },
		  zoom: {
				enabled: false
			}
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '47%',
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
          categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec'],
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
        },
		responsive: [{
			breakpoint: 575,
			options: {
				series: [{
				  name: 'Income',
				  data: [80, 24, 80, 90, 80, 70]
				}, {
				  name: 'Expense',
				  data: [40, 60, 20, 60, 60, 20]
				}, {
				  name: 'Others',
				  data: [20, 17, 5, 20, 20, 10]
				}],
				chart: {
				  height: 250,
				},
				 plotOptions: {
				  bar: {
					columnWidth: '65%'
				  },
				},
				xaxis: {
				  categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun'],
				},
			},
		}]

        };

        var chart = new ApexCharts(document.querySelector("#customerMap"), options);
        chart.render();
		
	}
	
	var customerMap2 = function(){
         var options = {
          series: [{
          name: 'Income',
          data: [80, 24, 80, 90, 80, 70, 20, 85, 80, 45, 25, 65]
        }, {
          name: 'Expense',
          data: [40, 60, 20, 60, 60, 20, 60, 25, 40, 65, 15, 40]
        }, {
          name: 'Others',
          data: [20, 17, 5, 20, 20, 10, 15, 10, 15, 20, 60, 15]
        }],
          chart: {
          type: 'bar',
          height: 400,
		  toolbar:{
			show:false
		  }
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '47%',
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
          categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec'],
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
        },
		responsive: [{
			breakpoint: 575,
			options: {
				series: [{
				  name: 'Income',
				  data: [80, 24, 80, 90, 80, 70]
				}, {
				  name: 'Expense',
				  data: [40, 60, 20, 60, 60, 20]
				}, {
				  name: 'Others',
				  data: [20, 17, 5, 20, 20, 10]
				}],
				chart: {
				  height: 250,
				},
				 plotOptions: {
				  bar: {
					columnWidth: '65%'
				  },
				},
				xaxis: {
				  categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun'],
				},
			},
		}]
		
        };

        var chart = new ApexCharts(document.querySelector("#customerMap2"), options);
        chart.render();
		
	}
	
	var customerMap3 = function(){
         var options = {
          series: [{
          name: 'Income',
          data: [80, 24, 80, 90, 80, 70, 20, 85, 80, 45, 25, 65]
        }, {
          name: 'Expense',
          data: [40, 60, 20, 60, 60, 20, 60, 25, 40, 65, 15, 40]
        }, {
          name: 'Others',
          data: [20, 17, 5, 20, 20, 10, 15, 10, 15, 20, 60, 15]
        }],
          chart: {
          type: 'bar',
          height: 400,
		  toolbar:{
			show:false
		  }
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '47%',
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
          categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec'],
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
        },
		
		responsive: [{
			breakpoint: 575,
			options: {
				series: [{
				  name: 'Income',
				  data: [80, 24, 80, 90, 80, 70]
				}, {
				  name: 'Expense',
				  data: [40, 60, 20, 60, 60, 20]
				}, {
				  name: 'Others',
				  data: [20, 17, 5, 20, 20, 10]
				}],
				chart: {
				  height: 250,
				},
				 plotOptions: {
				  bar: {
					columnWidth: '65%'
				  },
				},
				xaxis: {
				  categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun'],
				},
			},
		}]
		
        };

        var chart = new ApexCharts(document.querySelector("#customerMap3"), options);
        chart.render();
		
	}
	
	var widgetChart1 = function(){
		var options = {
		  series: [
			{
				name: 'Net Profit',
				data: [500, 500, 400, 400, 600, 600, 300, 300,500, 500,700,700],
				//radius: 12,	
			}, 				
		],
			chart: {
			type: 'area',
			height: 100,
			toolbar: {
				show: false,
			},
			zoom: {
				enabled: false
			},
			sparkline: {
				enabled: true
			}
			
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
		  width: 3,
		  curve:'straight',
		  colors:['#FFD54F'],
		},
		
		grid: {
			show:false,
			borderColor: 'rgba(255,255,255,0.08)',
			padding: {
				top: 0,
				right: 0,
				bottom: 0,
				left: 0

			}
		},
		states: {
                normal: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                hover: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                active: {
                    allowMultipleDataPointsSelection: false,
                    filter: {
                        type: 'none',
                        value: 0
                    }
                }
            },
		xaxis: {
			categories: ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',],
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false
			},
			labels: {
				show: false,
				style: {
					fontSize: '12px',
				}
			},
			crosshairs: {
				show: false,
				position: 'front',
				stroke: {
					width: 1,
					dashArray: 3
				}
			},
			tooltip: {
				enabled: true,
				formatter: undefined,
				offsetY: 0,
				style: {
					fontSize: '12px',
				}
			}
		},
		yaxis: {
			show: false,
		},
		fill: {
		  opacity: 0.28,
		  colors:['#FFD54F']
		},
		tooltip: {
			style: {
				fontSize: '12px',
			},
			y: {
				formatter: function(val) {
					return "$" + val + " thousands"
				}
			}
		}
		};

		var chartBar1 = new ApexCharts(document.querySelector("#widgetChart1"), options);
		chartBar1.render();
	 
	}
	var widgetChart2 = function(){
		var options = {
		  series: [
			{
				name: 'Net Profit',
				data: [500, 500, 300, 300, 600, 600, 400, 400,200, 200,500,500],
				//radius: 12,	
			}, 				
		],
			chart: {
			type: 'area',
			height: 100,
			toolbar: {
				show: false,
			},
			zoom: {
				enabled: false
			},
			sparkline: {
				enabled: true
			}
			
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
		  width: 3,
		  curve:'straight',
		  colors:['#FFD54F'],
		},
		
		grid: {
			show:false,
			borderColor: 'rgba(255,255,255,0.08)',
			padding: {
				top: 0,
				right: 0,
				bottom: 0,
				left: 0

			}
		},
		states: {
                normal: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                hover: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                active: {
                    allowMultipleDataPointsSelection: false,
                    filter: {
                        type: 'none',
                        value: 0
                    }
                }
            },
		xaxis: {
			categories: ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',],
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false
			},
			labels: {
				show: false,
				style: {
					fontSize: '12px',
				}
			},
			crosshairs: {
				show: false,
				position: 'front',
				stroke: {
					width: 1,
					dashArray: 3
				}
			},
			tooltip: {
				enabled: true,
				formatter: undefined,
				offsetY: 0,
				style: {
					fontSize: '12px',
				}
			}
		},
		yaxis: {
			show: false,
		},
		fill: {
		  opacity: 0.28,
		  colors:['#FFD54F']
		},
		tooltip: {
			style: {
				fontSize: '12px',
			},
			y: {
				formatter: function(val) {
					return "$" + val + " thousands"
				}
			}
		}
		};

		var chartBar1 = new ApexCharts(document.querySelector("#widgetChart2"), options);
		chartBar1.render();
	}
	var widgetChart3 = function(){
		var options = {
		  series: [
			{
				name: 'Net Profit',
				data: [300, 300, 400, 400, 200, 200, 400, 400,500, 500,700,700],
				//radius: 12,	
			}, 				
		],
			chart: {
			type: 'area',
			height: 100,
			toolbar: {
				show: false,
			},
			zoom: {
				enabled: false
			},
			sparkline: {
				enabled: true
			}
			
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
		  width: 3,
		  curve:'straight',
		  colors:['#FFD54F'],
		},
		
		grid: {
			show:false,
			borderColor: 'rgba(255,255,255,0.08)',
			padding: {
				top: 0,
				right: 0,
				bottom: 0,
				left: 0

			}
		},
		states: {
                normal: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                hover: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                active: {
                    allowMultipleDataPointsSelection: false,
                    filter: {
                        type: 'none',
                        value: 0
                    }
                }
            },
		xaxis: {
			categories: ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',],
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false
			},
			labels: {
				show: false,
				style: {
					fontSize: '12px',
				}
			},
			crosshairs: {
				show: false,
				position: 'front',
				stroke: {
					width: 1,
					dashArray: 3
				}
			},
			tooltip: {
				enabled: true,
				formatter: undefined,
				offsetY: 0,
				style: {
					fontSize: '12px',
				}
			}
		},
		yaxis: {
			show: false,
		},
		fill: {
		  opacity: 0.28,
		  colors:['#FFD54F']
		},
		tooltip: {
			style: {
				fontSize: '12px',
			},
			y: {
				formatter: function(val) {
					return "$" + val + " thousands"
				}
			}
		}
		};

		var chartBar1 = new ApexCharts(document.querySelector("#widgetChart3"), options);
		chartBar1.render();
	}
	
	
 
	/* Function ============ */
		return {
			init:function(){
			},
			
			
			load:function(){
					radialChart();
					widgetChart1();	
					widgetChart2();
					widgetChart3();
					customerMap();
					customerMap2();
					customerMap3();
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