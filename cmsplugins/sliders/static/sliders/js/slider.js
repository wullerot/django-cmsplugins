var Slider = ( function( $ ) {
    'use strict';

    var $sliders;

    var speed = 1000;
    var delay = 5000;

    var $body = $('body');
    var $doc = $( document );
    var $win = $( window );

    $.fn.slider = slider_plugin;

    $doc.ready( document_ready );

    function document_ready() {
        $('.plugin-slider').slider();
    };

    function slider_plugin() {
        $sliders = this;
        for( var i = 0; i < $sliders.length; i++ ) {
            init_slider( $sliders[ i ] );
        }
        return this;
    };

    function init_slider( slider ) {
        var timer;
        var $arrows;
        var $indicators;
        var animating = false;
        var dir = 1;
        var now = 0;
        var next = 1;
        var $slider = $( slider ).addClass('slider-js');
        var $slides = $('.slide', $slider).each( load_image );
        var $now = $( $slides[ now ] ).addClass('active');
        var $next = $( $slides[ next ] );
        var autoplay = $slider.data('autoplay');
        var arrows = $slider.data('arrows');
        var indicators = $slider.data('indicators');
        var max = $slides.length - 1;

        set_arrows();
        set_indicators();
        set_timer();

        function animate() {
            window.clearTimeout( timer );
            if ( !animating ) {
                animating = true;
                $now = $( $slides[ now ] );
                $next = $( $slides[ next ] );
                $now.animate({ left: (dir * -100) + '%' }, speed);
                $next.css({ display: 'block', left: (dir * 100) + '%'})
                     .animate({ left: '0' }, speed, animate_end);
            }
        };

        function animate_end( e ) {
            set_indicator();
            dir = 1;
            now = next;
            next = now < max ? now + 1 : 0;
            $now = $( $slides[ now ] );
            $next = $( $slides[ next ] );
            animating = false;
            set_timer();
        };

        function change_by_arrow( e ) {
            var $arrow = $( this );
            if( $arrow.hasClass('arrow-left') ) {
                dir = -1;
                next = now > 0 ? now - 1 : max;
            } else {
                dir = 1;
                next = now < max ? now + 1 : 0;
            }
            animate();
        };

        function change_by_indicator( e ) {
            var $indicator = $( this );
            var i = $indicator.data('index');
            if ( i != now && !animating) {
                next = i;
                dir = next > now ? 1 : -1;
                animate();
            }
        };

        function load_image() {
            var $slide = $( this );
            var $image = $('.slide-image', $slide );
            var src = $image.data('src');
            var $img = $( new Image() ).attr({ src: src });
            $image.css({ 'background-image': 'url(' + src + ')'});
            $image.find('.image').remove();
        };

        function set_arrows() {
            if ( arrows === true ) {
                $arrows = $('.arrow', $slider);
                $arrows.on('click', change_by_arrow);
            }
        };

        function set_indicator() {
            if ( indicators === true ) {
                $( $indicators[ now ] ).removeClass('a');
                $( $indicators[ next ] ).addClass('a');
            }
        }
        function set_indicators() {
            if ( indicators === true ) {
                $indicators = $('.indicator', $slider);
                for ( var i = 0; i < $indicators.length; i++ ) {
                    $indicators[ i ]._slide = $( $slides[ i ] );
                }
                $( $indicators[ now ] ).addClass('a');
                $indicators.on('click', change_by_indicator);
            }
        };

        function set_timer() {
            if( autoplay === true ) {
                timer = window.setTimeout(animate, delay);
            }
        };
    };

})( jQuery );
