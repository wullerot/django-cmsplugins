/*
Copyright (c) 2016, RouxCode
https://developers.google.com/maps/documentation/javascript/reference
*/

var StreetView = ( function() {
    'use strict';

    var apikey;
    var $plugins;

    $.fn.streetview = streetview_plugin;
    $('.plugin-streetview').streetview();

    function streetview_plugin() {
        $plugins = this;
        if( $plugins.length > 0 ) {
            GoogleAPI.register_callback(init);
        }
        return this;
    };

    function init() {
        for( var i = 0; i < $plugins.length; i++ ) {
            streetview( $plugins[ i ] );
        }
    };

    function streetview( plugin ) {
        var $plugin = $( plugin );
        var $view = $('.view', $plugin);
        var view = new google.maps.StreetViewPanorama($view[0], get_options());

        function get_options() {
            var options = {
                position: {
                    lat: $view.data('lat'),
                    lng: $view.data('lng')
                },
                disableDoubleClickZoom: $view.data('double_click_zoom'),
                scrollwheel: $view.data('scrollwheel'),
                zoomControl: $view.data('zoom_control'),
                zoom: 1
            }
            if ( $view.data('pan_heading') || $view.data('pan_pitch') ) {
                options['pov'] = {
                    heading: $view.data('pan_heading'),
                    pitch: $view.data('pan_pitch')
                }
            }
            return options;
        };
    };

    return {};

})( jQuery );
