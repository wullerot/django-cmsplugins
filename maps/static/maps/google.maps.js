/*
Copyright (c) 2016, RouxCode
https://developers.google.com/maps/documentation/javascript/reference
*/

var GoogleMap = ( function() {
    'use strict';

    var apikey;
    var $plugins;

    $.fn.googlemap = googlemap_plugin;
    $('.plugin-googlemaps').googlemap();

    function googlemap_plugin() {
        $plugins = this;
        if( $plugins.length > 0 ) {
            GoogleAPI.register_callback(init);
        }
        return this;
    };

    function init() {
        for( var i = 0; i < $plugins.length; i++ ) {
            map_plugin( $plugins[ i ] );
        }
    };

    function map_plugin( plugin ) {
        var info;
        var marker;
        var $plugin = $( plugin );
        var $map = $('.map', $plugin);
        var map = new google.maps.Map($map[0], get_options());

        set_style();
        set_marker();
        set_info();

        function get_options() {
            var options = {
                center: {
                    lat: $map.data('lat'),
                    lng: $map.data('lng')
                },
                draggable: $map.data('draggable'),
                disableAutoPan: false,
                disableDoubleClickZoom: $map.data('double_click_zoom'),
                keyboardShortcuts: $map.data('keyboard_shortcuts'),
                mapTypeId: google.maps.MapTypeId[$map.data('map_type')],
                panControl: $map.data('pan_control'),
                scrollwheel: $map.data('scrollwheel'),
                streetViewControl: $map.data('street_view_control'),
                zoom: $map.data('zoom')
            }
            return options;
        };

        function show_info() {
            info.open(map, marker);
        };

        function set_info() {
            var content = $map.data('info');
            if ( $map.data('info_image') ) {
                var src = document.location.origin + $map.data('info_image');
                content += '<br><br><img src="' + src + '">';
            }
            info = new google.maps.InfoWindow({content: content});
            google.maps.event.addListener(marker, 'click', show_info);
            if( $map.data('show_infowindow') ) {
                show_info();
                map.panBy(0, -80);
            }
        };

        function set_marker() {
            marker = new google.maps.Marker({
                map: map,
                position: new google.maps.LatLng(
                    $map.data('lat'),
                    $map.data('lng')
                )
            });
        };

        function set_style() {
            if ( $map.data('style') ) {
                map.setOptions({
                    styles: eval('(' + $map.data('style') + ')') }
                );
            }
        };
    };

    return {};

})( jQuery );
