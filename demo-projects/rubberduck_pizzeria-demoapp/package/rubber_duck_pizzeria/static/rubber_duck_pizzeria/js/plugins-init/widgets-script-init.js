(function($) {
    /* "use strict" */

 var dzChartlist = function(){
	
	var screenWidth = $(window).width();
	
	var activityChart = function(){
		/*======== 16. ANALYTICS - ACTIVITY CHART ========*/
		var activity = document.getElementById("activity");
		if (activity !== null) {
			var activityData = [{
					first: [35, 48, 25, 35, 40, 24, 30, 25, 22, 20, 45, 35]
				},
				{
					first: [50, 35, 35, 45, 40, 50, 60, 80, 25, 50, 34, 35]
				},
				{
					first: [20, 35, 60, 45, 40, 70, 30, 80, 65, 70, 60, 35]
				},
				{
					first: [25, 88, 25, 50, 70, 70, 60, 70, 50, 60, 50, 70]
				}
			];
			activity.height = 300;
			
			var config = {
				type: "bar",
				data: {
					labels: [
						"01",
						"02",
						"03",
						"04",
						"05",
						"06",
						"07",
						"08",
						"09",
						"10",
						"11",
						"12",
					],
					datasets: [
						{
							label: "My First dataset",
							data:  [35, 18, 30, 35, 40, 20, 30, 25, 22, 20, 45, 35],
							borderColor: 'rgba(250, 204, 21, 1)',
							borderWidth: "0",
							backgroundColor: 'rgba(250, 204, 21, 1)',
							
						}
					]
				},
				options: {
					responsive: true,
					maintainAspectRatio: false,
					plugins:{
						legend: false,
						tooltip: {
							//mode: "index",
							//intersect: false,
							//titleFontColor: "#888",
							//bodyFontColor: "#555",
							//titleFontSize: 12,
							//bodyFontSize: 15,
							//backgroundColor: "rgba(256,256,256,0.95)",
							//displayColors: true,
							//xPadding: 10,
							//yPadding: 7,
							//borderColor: "rgba(220, 220, 220, 0.9)",
							//borderWidth: 2,
							//caretSize: 6,
							//caretPadding: 10,
							enabled: true,
						}	
					},
					
					scales: {
						y:{
							grid: {
								color: "rgba(89, 59, 219,0.1)",
								drawBorder: true
							},
							ticks: {
								fontColor: "#999",
								stepSize: 5,
							},
						},
						x:{
							grid: {
								display: false,
								zeroLineColor: "transparent"
							},
							ticks: {
								stepSize: 5,
								fontColor: "#999",
								fontFamily: "Nunito, sans-serif"
							}
						}
					},
					
				}
			};

			var ctx = document.getElementById("activity").getContext("2d");
			var myLine = new Chart(ctx, config);

			var items = document.querySelectorAll("#user-activity .nav-tabs .nav-item");
			items.forEach(function(item, index) {
				item.addEventListener("click", function() {
					config.data.datasets[0].data = activityData[index].first;
					myLine.update();
				});
			});
		}
	}
	var activeUser = function(){
		if(jQuery('#activeUser').length > 0 ){
			var data = {
				labels: ["0", "1", "2", "3", "4", "5", "6", "0", "1", "2", "3", "4", "5", "6"],
				datasets: [{
					label: "My First dataset",
					backgroundColor: "rgba(58,223,174,1)",
					strokeColor: "rgba(58,223,174,1)",
					pointColor: "rgba(0,0,0,0)",
					pointStrokeColor: "rgba(58,223,174,1)",
					pointHighlightFill: "rgba(58,223,174,1)",
					pointHighlightStroke: "rgba(58,223,174,1)",
					data: [65, 59, 80, 81, 56, 55, 40, 65, 59, 80, 81, 56, 55, 40],
					barPercentage: 0.65,
				}]
			};

			var ctx = document.getElementById("activeUser").getContext("2d");
			var chart = new Chart(ctx, {
				type: "bar",
				data: data,
				options: {
					responsive: !0,
					maintainAspectRatio: false,
					plugins:{
						legend: {
							display: !1
						},
						tooltips: {
							enabled: false,
						},	
					},
					scales: {
						x:{
							display: !1,
							grid: {
								display: !1
							},
							categoryPercentage: 0.5
						},
						y:{
							display: !1,
							ticks: {
								padding: 10,
								stepSize: 20,
								max: 100,
								min: 0
							},
							grid: {
								display: !0,
								drawBorder: !1,
								lineWidth: 1,
								zeroLineColor: "#48f3c0"
							}
						}
					}
				}
			});
			
			setInterval(function() {
				chart.config.data.datasets[0].data.push(
					Math.floor(10 + Math.random() * 80)
				);
				chart.config.data.datasets[0].data.shift();
				chart.update();
			}, 2000);
			
		}
	}
	
	var chartWidget1 = function(){
		if(jQuery('#chart_widget_1').length > 0 ){
			
			const chart_widget_1 = document.getElementById("chart_widget_1").getContext('2d');
			//generate gradient
			// const gradientStroke = chart_widget_1.createLinearGradient(0, 0, 0, 250);
			// gradientStroke.addColorStop(0, "#00abc5");
			// gradientStroke.addColorStop(1, "#000080");

			// chart_widget_1.attr('height', '100');

			new Chart(chart_widget_1, {
				type: 'bar',
				data: {
					defaultFontFamily: 'Poppins',
					labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
					datasets: [
						{
							label: "My First dataset",
							data: [65, 59, 80, 81, 56, 55, 40],
							borderColor: 'rgba(255, 255, 255, .8)',
							borderWidth: "0",
							backgroundColor: 'rgba(255, 255, 255, .8)', 
							hoverBackgroundColor: 'rgba(255, 255, 255, .8)',
							barPercentage: 0.5, 
						}
					]
				},
				options: {
					plugins:{
						legend:false,
					},
					responsive: true, 
					maintainAspectRatio: false,  
					scales: {
						y:{
							display: false, 
							ticks: {
								beginAtZero: true, 
								display: false, 
								max: 100, 
								min: 0, 
								stepSize: 10
							}, 
							grid: {
								display: false, 
								drawBorder: false
							}
						},
						x:{
							display: false, 
							grid: {
								display: false, 
								drawBorder: false
							}, 
							ticks: {
								display: false
							}
						}
					}
				}
			});
		}
	}
	
	var chartWidget2 = function(){
		//#chart_widget_2
		if(jQuery('#chart_widget_2').length > 0 ){
			
			const chart_widget_2 = document.getElementById("chart_widget_2").getContext('2d');
			//generate gradient
			const chart_widget_2gradientStroke = chart_widget_2.createLinearGradient(0, 0, 0, 250);
			chart_widget_2gradientStroke.addColorStop(0, "#430b58");
			chart_widget_2gradientStroke.addColorStop(1, "#6c2586");

			// chart_widget_2.attr('height', '100');

			new Chart(chart_widget_2, {
				type: 'bar',
				data: {
					defaultFontFamily: 'Poppins',
					labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
					datasets: [
						{
							label: "My First dataset",
							data: [65, 59, 80, 81, 56, 55, 40, 88, 45, 95, 54, 76],
							borderColor: chart_widget_2gradientStroke,
							borderWidth: "0",
							backgroundColor: chart_widget_2gradientStroke, 
							hoverBackgroundColor: chart_widget_2gradientStroke,
							barPercentage: 0.1, 
						}
					]
				},
				options: {
					plugins:{
						legend:false,
					},
					responsive: true, 
					maintainAspectRatio: false,  
					scales: {
						y:{
							display: false, 
							ticks: {
								beginAtZero: true, 
								display: false, 
								max: 100, 
								min: 0, 
								stepSize: 10
							}, 
							grid: {
								display: false, 
								drawBorder: false
							}
						},
						x:{
							display: false, 
							grid: {
								display: false, 
								drawBorder: false
							}, 
							ticks: {
								display: false
							}
						}
					}
				}
			});

		}
	}
	
	
	var chartWidget3 = function(){
		//#chart_widget_3
		if(jQuery('#chart_widget_3').length > 0 ){
		const chart_widget_3 = document.getElementById("chart_widget_3").getContext('2d');
		
		// chart_widget_3.height = 100;

		let barChartData = {
			defaultFontFamily: 'Poppins',
			labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
			datasets: [{
				label: 'Expense',
				backgroundColor: '#ff2c53',
				hoverBackgroundColor: '#ff5777',  
				barPercentage: 0.2,
				data: [
					'20',
					'14',
					'18',
					'25',
					'27',
					'22',
					'12', 
					'24', 
					'20', 
					'14', 
					'18', 
					'16'
				]
			}, {
				label: 'Earning',
				backgroundColor: '#F1F3F7',
				hoverBackgroundColor: '#F1F3F7', 
				barPercentage: 0.2,
				data: [
					'12',
					'18',
					'14',
					'7',
					'5',
					'10',
					'20', 
					'8', 
					'12', 
					'18', 
					'14', 
					'16'
				]
			}]

		};

		new Chart(chart_widget_3, {
			type: 'bar',
			data: barChartData,
			options: {
				plugins:{
					legend:false,
					tooltip: {
						mode: 'index',
						intersect: false
					},
					
				},
				title: {
					display: false
				},
				responsive: true,
				maintainAspectRatio: false, 
				scales: {
					x:{
						display: false, 
						stacked: true,
						 
						ticks: {
							display: false
						}, 
						grid: {
							display: false, 
							drawBorder: false
						}
					},
					y:{
						display: false, 
						stacked: true, 
						grid: {
							display: false, 
							drawBorder: false
						}, 
						ticks: {
							display: false
						}
					}
				}
			}
		});
		}

	}
	
	var chartWidget4 = function(){
		//#chart_widget_4
		if(jQuery('#chart_widget_4').length > 0 ){

		const chart_widget_4 = document.getElementById("chart_widget_4").getContext('2d');
		
		// chart_widget_4.height = 100;

		let barChartData2 = {
			defaultFontFamily: 'Poppins',
			labels: ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'],
			datasets: [{
				label: 'Expense',
				backgroundColor: '#430b58',
				hoverBackgroundColor: '#6c2586', 
				barPercentage: 1, 
				barThickness: 5, 
				data: [
					'20',
					'14',
					'18',
					'25',
					'27',
					'22',
					'12', 
					'24', 
					'20', 
					'14', 
					'18', 
					'16', 
					'34', 
					'32', 
					'43', 
					'36', 
					'56', 
					'12', 
					'23', 
					'34'
				]
			}, {
				label: 'Earning',
				backgroundColor: '#F1F3F7',
				hoverBackgroundColor: '#F1F3F7', 
				barPercentage: 1, 
				barThickness: 5, 
				data: [
					'32',
					'58',
					'34',
					'37',
					'15',
					'41',
					'24', 
					'38', 
					'52', 
					'38', 
					'24', 
					'19', 
					'54', 
					'34', 
					'23', 
					'34', 
					'35', 
					'22', 
					'43', 
					'33'
				]
			}]

		};

		new Chart(chart_widget_4, {
			type: 'bar',
			data: barChartData2,
			options: {
				plugins:{
					legend:false,
					tooltip: {
						mode: 'index',
						intersect: false
					},
					
				},
				title: {
					display: false
				},
				responsive: true,
				maintainAspectRatio: false, 
				scales: {
					x:{
						display: false, 
						stacked: true,
						
						ticks: {
							display: false
						}, 
						grid: {
							display: false, 
							drawBorder: false
						}
					},
					y:{
						display: false, 
						stacked: true, 
						grid: {
							display: false, 
							drawBorder: false
						}, 
						ticks: {
							display: false, 
							max: 100, 
							min: 0
						}
					}
				}
			}
		});

		}
	}
	
	
	var chartWidget5 = function(){
		
		
		
		//#chart_widget_5
		if(jQuery('#chart_widget_5').length > 0 ){
				chartReinitialize('#chart_widget_5');
				
			new Chartist.Line("#chart_widget_5", {
				labels: ["1", "2", "3", "4", "5", "6", "7", "8"],
				series: [
					[4, 5, 1.5, 6, 7, 5.5, 5.8, 4.6]
				]
			}, {
				low: 0,
				showArea: 1,
				showPoint: !0,
				showLine: !0,
				fullWidth: !0,
				lineSmooth: !1,
				chartPadding: {
					top: 4,
					right: 0,
					bottom: 0,
					left: 0
				},
				axisX: {
					showLabel: !1,
					showGrid: !1,
					offset: 0
				},
				axisY: {
					showLabel: !1,
					showGrid: !1,
					offset: 0
				}
			});
		}
	}
	
	var chartWidget6 = function(){
		//#chart_widget_6
		if(jQuery('#chart_widget_6').length > 0 ){
			
			new Chartist.Line("#chart_widget_6", {
				labels: ["1", "2", "3", "4", "5", "6", "7", "8"],
				series: [
					[4, 5, 3.5, 5, 4, 5.5, 3.8, 4.6]
				]
			}, {
				low: 0,
				showArea: 1,
				showPoint: !0,
				showLine: !0,
				fullWidth: !0,
				lineSmooth: !1,
				chartPadding: {
					top: 4,
					right: 0,
					bottom: 0,
					left: 0
				},
				axisX: {
					showLabel: !1,
					showGrid: !1,
					offset: 0
				},
				axisY: {
					showLabel: !1,
					showGrid: !1,
					offset: 0
				}
			});
		}
	}
	
	var chartWidget7 = function(){
		
		//#chart_widget_7
		if(jQuery('#chart_widget_7').length > 0 ){
			chartReinitialize('#chart_widget_7');
		const chart_widget_7 = document.getElementById("chart_widget_7").getContext('2d');
		//generate gradient
		const chart_widget_7gradientStroke = chart_widget_7.createLinearGradient(0, 0, 0, 250);
		chart_widget_7gradientStroke.addColorStop(0, "#ff2c53");
		chart_widget_7gradientStroke.addColorStop(1, "#ff2c53");

			// chart_widget_7.attr('height', '100');

			new Chart(chart_widget_7, {
				type: 'bar',
				data: {
					defaultFontFamily: 'Poppins',
					labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
					datasets: [
						{
							label: "My First dataset",
							data: [65, 59, 80, 81, 56, 55, 40, 88, 45, 95, 54, 76],
							borderColor: chart_widget_7gradientStroke,
							borderWidth: "0",
							backgroundColor: chart_widget_7gradientStroke, 
							hoverBackgroundColor: chart_widget_7gradientStroke,
							barPercentage: 0.6, 
						}
					]
				},
				options: {
					plugins:{
						legend:false,
						
					},
					responsive: true, 
					maintainAspectRatio: false,  
					scales: {
						y:{
							display: false, 
							max: 100, 
							min: 0, 
							ticks: {
								beginAtZero: true, 
								display: false, 
								stepSize: 10
							}, 
							grid: {
								display: false, 
								drawBorder: false
							}
						},
						x:{
							display: false,
							grid: {
								display: false, 
								drawBorder: false
							}, 
							ticks: {
								display: false
							}
						}
					}
				}
			});
		}
	}
	
	var chartWidget8 = function(){
		//#chart_widget_8
		if(jQuery('#chart_widget_8').length > 0 ){
			
			new Chartist.Line("#chart_widget_8", {
				labels: ["1", "2", "3", "4", "5", "6", "7", "8"],
				series: [
					[4, 5, 1.5, 6, 7, 5.5, 5.8, 4.6]
				]
			}, {
				low: 0,
				showArea: !1,
				showPoint: !0,
				showLine: !0,
				fullWidth: !0,
				lineSmooth: !1,
				chartPadding: {
					top: 4,
					right: 0,
					bottom: 0,
					left: 0
				},
				axisX: {
					showLabel: !1,
					showGrid: !1,
					offset: 0
				},
				axisY: {
					showLabel: !1,
					showGrid: !1,
					offset: 0
				}
			});

		}
	}
	
	var chartWidget9 = function(){
		//#chart_widget_9
		if(jQuery('#chart_widget_9').length > 0 ){
		const chart_widget_9 = document.getElementById("chart_widget_9").getContext('2d');
		new Chart(chart_widget_9, {
			type: "line",
			data: {
				labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "January", "February", "March", "April"],
				datasets: [{
					label: "Sales Stats",
					backgroundColor: "#2780d4",
					borderColor: '#2780d4',
					pointBackgroundColor: '#2780d4',
					pointBorderColor: '#2780d4',
					pointHoverBackgroundColor: '#2780d4',
					pointHoverBorderColor: '#2780d4',
					fill:true,
					data: [20, 10, 18, 15, 32, 18, 15, 22, 8, 6, 12, 13, 10, 18, 14, 24, 16, 12, 19, 21, 16, 14, 24, 21, 13, 15, 27, 29, 21, 11, 14, 19, 21, 17]
				}]
			},
			options: {
				title: {
					display: !1
				},
				plugins:{
					legend:false,
					tooltip: {
						intersect: !1,
						mode: "nearest",
						xPadding: 10,
						yPadding: 10,
						caretPadding: 10
					},
					
				},
				
				responsive: !0,
				maintainAspectRatio: !1,
				hover: {
					mode: "index"
				},
				scales: {
					x:{
						display: !1,
						grid: !1,
						scaleLabel: {
							display: !0,
							labelString: "Month"
						}
					},
					y:{
						display: !1,
						grid: !1,
						scaleLabel: {
							display: !0,
							labelString: "Value"
						},
						ticks: {
							beginAtZero: !0
						}
					}
				},
				elements: {
					line: {
						tension: .15
					},
					point: {
						radius: 2,
						borderWidth: 1
					}
				},
				layout: {
					padding: {
						left: 0,
						right: 0,
						top: 5,
						bottom: 0
					}
				}
			}
		});

		}
	}
	
	var chartWidget10 = function(){
		//#chart_widget_10
		if(jQuery('#chart_widget_10').length > 0 ){

		const chart_widget_10 = document.getElementById("chart_widget_10").getContext('2d');

		new Chart(chart_widget_10, {
			type: "line",
			data: {
				labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
				datasets: [{
					label: "Sales Stats",
					backgroundColor: "#2780d4",
					borderColor: '#2780d4',
					pointBackgroundColor: '#2780d4',
					pointBorderColor: '#2780d4',
					pointHoverBackgroundColor: '#2780d4',
					pointHoverBorderColor: '#2780d4',
					borderWidth: 0, 
					fill:true,
					data: [20, 10, 18, 10, 32, 15, 15, 22, 18, 6, 12, 13]
				}]
			},
			options: {
				title: {
					display: !1
				},
				plugins:{
					legend:false,
					tooltip: {
						intersect: !1,
						mode: "nearest",
						xPadding: 10,
						yPadding: 10,
						caretPadding: 10
					},
					
				},
				
				responsive: !0,
				maintainAspectRatio: !1,
				hover: {
					mode: "index"
				},
				scales: {
					x:{
						display: !1,
						grid: !1,
						scaleLabel: {
							display: !0,
							labelString: "Month"
						}
					},
					y:{
						display: !1,
						grid: !1,
						scaleLabel: {
							display: !0,
							labelString: "Value"
						},
						ticks: {
							beginAtZero: !0
						}
					}
				},
				elements: {
					line: {
						tension: .7
					},
					point: {
						radius: 0,
						borderWidth: 0
					}
				},
				layout: {
					padding: {
						left: 0,
						right: 0,
						top: 5,
						bottom: 0
					}
				}
			}
		});

		}
	}
	
	var chartWidget11 = function(){

		//#chart_widget_11
		if(jQuery('#chart_widget_11').length > 0 ){
		const chart_widget_11 = document.getElementById("chart_widget_11").getContext('2d');
		new Chart(chart_widget_11, {
			type: "line",
			data: {
				labels: ["January", "February", "March", "April", "May", "June"],
				datasets: [{
					label: "Sales Stats",
					backgroundColor: "rgba(120, 120, 120, .5)",
					borderColor: '#787878',
					pointBackgroundColor: '#787878',
					pointBorderColor: '#787878',
					pointHoverBackgroundColor: '#787878',
					pointHoverBorderColor: '#787878',
					fill:true,
					data: [0, 18, 14, 24, 16, 30]
				}]
			},
			options: {
				title: {
					display: !1
				},
				plugins:{
					legend:false,
					tooltip: {
						intersect: !1,
						mode: "nearest",
						xPadding: 5,
						yPadding: 5,
						caretPadding: 5
					},
					
				},
				responsive: !0,
				maintainAspectRatio: !1,
				hover: {
					mode: "index"
				},
				scales: {
					x:{
						display: !1,
						grid: !1,
						scaleLabel: {
							display: !0,
							labelString: "Month"
						}, 
						ticks: {
							max: 30, 
							min: 0
						}
					},
					y:{
						display: !1,
						grid: !1,
						scaleLabel: {
							display: !0,
							labelString: "Value"
						},
						ticks: {
							beginAtZero: !0
						}
					}
				},
				elements: {
					line: {
						tension: .15
					},
					point: {
						radius: 2,
						borderWidth: 1
					}
				},
				layout: {
					padding: {
						left: 0,
						right: 0,
						top: 0,
						bottom: 0
					}
				}
			}
		});
		}
	}
	
	var chartWidget14 = function(){
	
		//#chart_widget_14
		if(jQuery('#chart_widget_14').length > 0 ){
		const chart_widget_14 = document.getElementById("chart_widget_14");
		chart_widget_14.height = 200;
		new Chart(chart_widget_14, {
			type: 'line',
			data: {
				defaultFontFamily: 'Poppins',
				labels: ["Jan", "Febr", "Mar", "Apr", "May", "Jun", "Jul"],
				datasets: [
					{
						label: "My First dataset",
						data: [55, 30, 90, 41, 86, 45, 80],
						borderColor: '#3693FF',
						borderWidth: "2",
						backgroundColor: 'transparent',  
						pointBackgroundColor: '#3693FF', 
						pointRadius: 0,
						tension:0.5,
					}
				]
			},
			options: {
				plugins:{
					legend:false,
				},
				responsive: true, 
				maintainAspectRatio: false, 
				scales: {
					y:{
						display: false, 
						max: 100, 
						min: 0, 
						ticks: {
							beginAtZero: true, 
							stepSize: 20, 
							padding: 0, 
							display: false, 
						}, 
						grid: {
							drawBorder: false, 
							display: false
						}
					},
					x:{
						display: false, 
						ticks: {
							padding: 0, 
							display: false
						}, 
						grid: {
							display: false, 
							drawBorder: false
						}
					}
				}
			}
		});
		}
	}
	
	var chartWidget15 = function(){
	
		//#chart_widget_15
		if(jQuery('#chart_widget_15').length > 0 ){
		const chart_widget_15 = document.getElementById("chart_widget_15");
		chart_widget_15.height = 200;
		new Chart(chart_widget_15, {
			type: 'line',
			data: {
				defaultFontFamily: 'Poppins',
				labels: ["Jan", "Febr", "Mar", "Apr", "May", "Jun", "Jul"],
				datasets: [
					{
						label: "My First dataset",
						data: [25, 60, 30, 71, 26, 85, 50],
						borderColor: '#2780d4',
						borderWidth: "2",
						backgroundColor: 'transparent',  
						pointBackgroundColor: '#2780d4', 
						pointRadius: 0,
						tension:0.5,
					}
				]
			},
			options: {
				plugins:{
					legend:false,
				}, 
				responsive: true, 
				maintainAspectRatio: false, 
				scales: {
					y:{
						display: false, 
						max: 100, 
						min: 0, 
						ticks: {
							beginAtZero: true, 
							stepSize: 20, 
							padding: 0, 
							display: false, 
						}, 
						grid: {
							drawBorder: false, 
							display: false
						}
					},
					x:{
						display: false, 
						ticks: {
							padding: 0, 
							display: false
						}, 
						grid: {
							display: false, 
							drawBorder: false
						}
					}
				}
			}
		});
		}
	}
	
	var chartWidget16 = function(){
		//#chart_widget_16
		if(jQuery('#chart_widget_16').length > 0 ){

			const chart_widget_16 = document.getElementById("chart_widget_16");
			
			chart_widget_16.height = 345;

			new Chart(chart_widget_16, {
				type: 'line',
				data: {
					defaultFontFamily: 'Poppins',
					labels: ["Jan", "Febr", "Mar", "Apr", "May", "Jun", "Jul"],
					datasets: [
						{
							label: "My First dataset",
							data: [25, 60, 30, 71, 26, 85, 50],
							borderColor: 'rgba(250, 204, 21, 1)',
							borderWidth: "2",
							backgroundColor: 'rgba(250, 204, 21, 1)',  
							pointBackgroundColor: 'rgba(250, 204, 21, 1)',  
							tension:0.5,
							fill:true,
							pointRadius: 0
						}
					]
				},
				options: {
					plugins:{
						legend:false,
						tooltip: {
							intersect: !1,
							mode: "nearest",
							xPadding: 10,
							yPadding: 10,
							caretPadding: 10
						}, 
						
					},
					responsive: true, 
					maintainAspectRatio: false,
					scales: {
						y:{
							display: false, 
							max: 100, 
							min: 0, 
							ticks: {
								beginAtZero: true, 
								stepSize: 20, 
								padding: 0, 
								display: false, 
							}, 
							grid: {
								drawBorder: false, 
								display: false
							}
						},
						x:{
							display: false, 
							ticks: {
								padding: 0, 
								display: false, 
								beginAtZero: true
							}, 
							grid: {
								display: false, 
								drawBorder: false
							}
						}
					}
				}
			});
		}
	}
	
	var chartWidget17 = function(){
		//#chart_widget_17
		if(jQuery('#chart_widget_17').length > 0 ){

			let data = [];
			const totalPoints = 50;

			function getRandomData() {
				if (data.length > 0)
					data = data.slice(1);
				while (data.length < totalPoints) {
					var prev = data.length > 0 ? data[data.length - 1] : 50,
						y = prev + Math.random() * 10 - 5;
					if (y < 0) {
						y = 0;
					} else if (y > 100) {
						y = 100;
					}
					data.push(y);
				}
				const res = [];
				for (let i = 0; i < data.length; ++i) {
					res.push([i, data[i]])
				}
				return res; 
				
			}

			// Set up the control widget
			const updateInterval = 1000;

				if(jQuery('#chart_widget_17').length > 0 ){
			
				 const chart = jQuery.plot('#chart_widget_17', [getRandomData()], {
					colors: ['#430b58'],
					series: {
						lines: {
							show: true,
							lineWidth: 0,
							fill: 0.9
						},
						shadowSize: 0	// Drawing is faster without shadows
					},
					plugins:{
						legend:false,
					},
					grid: {
						borderColor: 'transparent',
						borderWidth: 0,
						labelMargin: 0
					},
					x: {
						color: 'transparent',
						font: {
							size: 10,
							color: '#fff'
						}
					},
					y: {
						min: 0,
						max: 100,
						color: 'transparent',
						font: {
							size: 10,
							color: '#fff'
						}
					}
				}); 

				function update_chart() {
					chart.setData([getRandomData()]);
					chart.draw();
					setTimeout(update_chart, updateInterval);
				}
			
				update_chart();
				
			}
		}
	}
	
	var widgetSparkLinedash = function(){
		/* Widget */
		if(jQuery('#widget_sparklinedash').length > 0 ){	 
			 $("#widget_sparklinedash").sparkline([10, 15, 26, 27, 28, 31, 34, 40, 41, 44, 49, 64, 68, 69, 72], {
				type: "bar",
				height: "40",
				width: "40",
				barWidth: "3",
				resize: !0,
				barSpacing: "3",
				barColor: "rgb(0, 171, 197)"
			});
		}
	}
	var widgetSparkBar = function(){
		if(jQuery('#widget_spark-bar').length > 0 ){	
			$("#widget_spark-bar").sparkline([33, 22, 68, 54, 8, 30, 74, 7, 36, 5, 41, 19, 43, 29, 38], {
				type: "bar",
				height: "40",
				barWidth: 3,
				barSpacing: 3,
				barColor: "rgb(7, 135, 234)"
			});
		}	
	}	
	var widgetStackedBarChart = function(){
		if(jQuery('#widget_StackedBarChart').length > 0 ){	
			$('#widget_StackedBarChart').sparkline([
				[1, 4, 2],
				[2, 3, 2],
				[3, 2, 2],
				[4, 1, 2]
			], {
					type: "bar",
					height: "40",
					barWidth: 3,
					barSpacing: 3, 
					stackedBarColor: ['#36b9d8', '#4bffa2', 'rgba(68, 0, 235, .8)']
				});
		}
	}
	var widgetTristate = function(){
		if(jQuery('#widget_tristate').length > 0 ){	

			$("#widget_tristate").sparkline([1, 1, 0, 1, -1, -1, 1, -1, 0, 0, 1, 1], {
				type: 'tristate',
				height: "40",
				barWidth: 3,
				barSpacing: 3, 
				colorMap: ['#36b9d8', '#4bffa2', 'rgba(68, 0, 235, .8)'], 
				negBarColor: 'rgba(245, 60, 121, .8)'
			});
		}
	}
	var widgetCompositeBar = function(){
			// Composite
		if(jQuery('#widget_composite-bar').length > 0 ){
			$("#widget_composite-bar").sparkline([73, 53, 50, 67, 3, 56, 19, 59, 37, 32, 40, 26, 71, 19, 4, 53, 55, 31, 37, 67, 10, 21], {
				type: "bar",
				height: "40",
				barWidth: "3",
				resize: !0,
				// barSpacing: "7",
				barColor: "rgb(68, 11, 89)", 
				width: '100%'
			});
		}	
	}

	var chartReinitialize = function(selector, notInList = []){
		jQuery(selector).empty();
		jQuery(selector).each(function() {
		  var attributes = $.map(this.attributes, function(item) {
			return item.name;
		  });

		  var thisObj = $(this);
		  $.each(attributes, function(i, item) {
			if(item != 'id' && (notInList.length === 0 || jQuery.inArray(item, notInList) === -1 )){
				thisObj.removeAttr(item);
			}
		  });
		});
		
	}	
	
	/* Function ============ */
		return {
			init:function(){
			},
			
			
			load:function(){
				 activityChart();	
				activeUser();
				chartWidget1();	
				chartWidget2();	
				chartWidget3();		
				chartWidget4();
				chartWidget5();
				chartWidget6();
				chartWidget7();
				chartWidget8(); 
				chartWidget9();
				chartWidget10();
				chartWidget11();
				chartWidget14();
				chartWidget15();
				chartWidget16();
				chartWidget17();
				widgetSparkLinedash(); 
				widgetSparkBar();
				widgetStackedBarChart();
				widgetTristate();
				widgetCompositeBar();
			},
			
			resize:function(){
				chartWidget5();
				chartWidget6();
				chartWidget7();
				chartWidget8();
			}
		}
	
	}();

	jQuery(document).ready(function(){
	});
		
	jQuery(window).on('load',function(){
		dzChartlist.load();
	});

	jQuery(window).on('resize',function(){
		setTimeout(function(){
			dzChartlist.resize();	
		}, 500);
		
	});     

})(jQuery);