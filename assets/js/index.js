$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    if(scroll < 600){
    $('.fixed-top').css('background', 'transparent');
    } else{
    $('.fixed-top').css('background', 'rgba(23, 162, 184, 0.9)');
    }
    });
