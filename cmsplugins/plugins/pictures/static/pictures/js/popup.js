function set_popup_gallery( selector, delegate ) {
    var d = delegate || 'a';
    var s = selector || '.popup-gallery';
    if( !is_edit_mode ) {
        var $galleries = $( s );
        for ( var i = 0; i < $galleries.length; i++ ) {
            var $gallery = $( $galleries[0] );
            $gallery.magnificPopup({
                delegate: d,
                type: 'image',
                gallery: { enabled: true }
            });
        }
    }
};

function set_popup_image( selector ) {
    var s = selector || '.popup-image';
    if( !is_edit_mode ) {
        $( s ).magnificPopup({ type: 'image' });
    }
};
