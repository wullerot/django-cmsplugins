var LazyLoadImage = ( function ( $ ) {
    'use strict';

    var $images;

    $.fn.lazyload_image = lazyload_image;
    $('.lazyload').lazyload_image();

    function lazyload_image() {
        $images = this;
        for( var i = 0; i < $images.length; i++ ) {
            init_image( $images[ i ] );
        }
        return this;
    };

    function init_image( image ) {
        var $image = $( image );
        var img = new Image();
        var src = $image.data('src');
        img.onload = loaded;
        img.src = src;


        function loaded() {
            if ( $image.is('img') ) {
                image.src = src;
            } else {
                $image.css({ 'background-image': 'url(' + src + ')'});
            }
        }
    };

})( jQuery );
