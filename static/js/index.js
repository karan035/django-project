$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    if(scroll < 600){
    $('.fixed-top').css('background', 'transparent');
    } else{
    $('.fixed-top').css('background', 'rgba(23, 162, 184, 0.9)');
    }
    });
    $(document).ready(function(){
		$('.gimg1').waypoint(function(direction){
			$('.gimg1').addClass('animated zoomIn')
		},{
			offset:'200px'
		})
	});
	$(document).ready(function(){
		$('.gimg2').waypoint(function(direction){
			$('.gimg2').addClass('animated zoomIn')
		},{
			offset:'200px'
		})
	});
	$(document).ready(function(){
		$('.gimg3').waypoint(function(direction){
			$('.gimg3').addClass('animated zoomIn')
		},{
			offset:'200px'
		})
	});
	$(document).ready(function(){
		$('.gimg4').waypoint(function(direction){
			$('.gimg4').addClass('animated zoomIn')
		},{
			offset:'400px'
		})
	});
	$(document).ready(function(){
		$('.gimg5').waypoint(function(direction){
			$('.gimg5').addClass('animated zoomIn')
		},{
			offset:'400px'
		})
	});
	$(document).ready(function(){
		$('.gimg6').waypoint(function(direction){
			$('.gimg6').addClass('animated zoomIn')
		},{
			offset:'400px'
		})
	});
	