var GoogleAPI = ( function( $ ) {
    'use strict';

    var apisrc = 'https://maps.google.com/maps/api/js';
    var lang = $( 'html' ).attr( 'lang' );
    var callback_list = [];
    var $doc = $( document );

    $doc.ready( load_api );

    function load_api() {
        var $apikey = $('.google-apikey:first');
        if ( $apikey.length > 0 ) {
            var apikey = $apikey.data('apikey')
            var url = apisrc + '?callback=GoogleAPI.loaded_api&key=' + apikey;
            if( lang ) {
                url = url + '&language=' + lang;
            }
            $.getScript( url );
        }
    };

    function loaded_api() {
        for ( var i = 0; i < callback_list.length; i ++ ) {
            callback_list[i]();
        }
    };

    function register_callback( func ) {
        callback_list.push(func);
    };

    return  {
        loaded_api: loaded_api,
        register_callback: register_callback
    };
})( jQuery );
