$(document).ready(function() {

    $(window).scroll(function() {
        var scrollTop = $(window).scrollTop();
        if (scrollTop != 0)
            $('#nav').stop().animate({
                'opacity': '0'
            }, 400);
        else
            $('#nav').stop().animate({
                'opacity': '1'
            }, 400);
    });

    $('#nav').hover(
        function(e) {
            var scrollTop = $(window).scrollTop();
            if (scrollTop != 0) {
                $('#nav').stop().animate({
                    'opacity': '1'
                }, 400);
            }
        },
        function(e) {
            var scrollTop = $(window).scrollTop();
            if (scrollTop != 0) {
                $('#nav').stop().animate({
                    'opacity': '0'
                }, 400);
            }
        }
    );


    //configuration
    var width = 720;
    var animationSpeed = 3000;
    var pause = 3000;
    var currentSlide = 1;

    //cache DOM
    var $slider = $('#slider');
    var $slideContainer = $slider.find('.slides');
    var $slides = $slideContainer.find('.slide');

    var interval;

    function startSlider() {
        interval = setInterval(function() {
            $slideContainer.animate({
                'margin-left': '-=' + width
            }, animationSpeed, function() {
                currentSlide++;
                if (currentSlide === $slides.length) {
                    currentSlide = 1;
                    $slideContainer.css('margin-left', 0);
                }
            });
        }, pause);
    }

    function pauseSlider() {
        clearInterval(interval);
    }


    $slider.on('mouseenter', pauseSlider).on('mouseleave', startSlider);

    startSlider();
    //setInterval
    //animate margin-left
    //if it's left slide, go to position 1 (0px)

    //listen for mouseenter and pause
    //resume on mouseleave

});
