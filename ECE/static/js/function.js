var $ = jQuery.noConflict();
$(document).ready(function () {

	jQuery('.header-menu').flexMenu({ responsivePattern: 'toggle'}); 
//flex-menu
	
	jQuery('.menu-icon').click(function(){ 
		jQuery(this).toggleClass('close-menu'); 
	}); 
	
	
	$('#course-carousal').owlCarousel({
		loop: true,
		margin: 10,
		responsiveClass: true,
		responsive: {
		  0: {
			items: 1,
			nav: true
		  },
		  600: {
			items: 2,
			nav: false
		  },
		  1000: {
			items: 3,
			nav: true,
			loop: false,
			margin: 20
		  }
		}
		})
		/****************************************** */
		$('#news-carousal').owlCarousel({
			loop: true,
			margin: 10,
			responsiveClass: true,
			responsive: {
				0: {
				items: 1,
				nav: true
				},
				600: {
				items: 2,
				nav: false
				},
				1000: {
				items: 3,
				nav: true,
				loop: false,
				margin: 20
				}
			}
			})
		
			/****************************************** */
		$('#event-slider').owlCarousel({
			loop: true,
			margin: 10,
			responsiveClass: true,
			responsive: {
				0: {
				items: 1,
				nav: true
				},
				600: {
				items: 2,
				nav: false
				},
				1000: {
				items: 3,
				nav: true,
				loop: false,
				margin: 20
				}
			}
			})

			/****************************************** */
		$('#testimonial-slider').owlCarousel({
			loop: true,
			margin: 10,
			responsiveClass: true,
			responsive: {
				0: {
				items: 1,
				nav: true
				},
				600: {
				items: 1,
				nav: false
				},
				1000: {
				items: 2,
				nav: true,
				loop: false,
				margin: 20
				}
			}
			})
			
})