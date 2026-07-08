/* JavaScript Document */
function carouselReview(){
	jQuery('.testimonial-one').owlCarousel({
		loop:true,
		autoplay:true,
		margin:20,
		nav:false,
		rtl:true,
		dots: false,
		navText: ['', ''],
		responsive:{
			0:{
				items:3
			},
			450:{
				items:4
			},
			600:{
				items:5
			},	
			991:{
				items:5
			},			
			
			1200:{
				items:7
			},
			1601:{
				items:5
			}
		}
	})
	jQuery('.cards-slider').owlCarousel({
		loop:false,
		margin:30,
		nav:true,
		rtl:(getUrlParams('dir') == 'rtl')?true:false,
		autoWidth:true,
		//rtl:true,
		dots: false,
		navText: ['', ''],
	})
}


jQuery(window).on('load',function(){
	setTimeout(function(){
		carouselReview();
	}, 1000); 
});
/* Document .ready END */