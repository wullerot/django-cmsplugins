from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin import defaults


GALLERY_CSS_CLASSES = getattr(
    settings,
    'PICTURES_GALLERY_CSS_CLASSES',
    defaults.CSS_CLASSES
)
GALLERY_HEIGHTS = getattr(
    settings,
    'PICTURES_GALLERY_HEIGHTS',
    defaults.HEIGHTS
)
GALLERY_WIDTHS = getattr(
    settings,
    'PICTURES_GALLERY_WIDTHS',
    defaults.WIDTHS
)
GALLERY_FIELDSETS = getattr(
    settings,
    'PICTURES_GALLERY_FIELDSETS',
    (
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': ['name', 'abstract', 'description'],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                # 'layout', # TODO add other layouts
                'width',
                'height',
                'is_visible',
                'in_navigation',
                'css_class',
            ],
        }),
    )
)
GALLERY_LAYOUTS = getattr(
    settings,
    'PICTURES_GALLERY_LAYOUTS',
    ['standard']
)
GALLERY_PLUGINS = getattr(
    settings,
    'PICTURES_GALLERY_PLUGINS',
    ['GalleryPicturePlugin']
)


GALLERYPICTURE_CSS_CLASSES = getattr(
    settings,
    'PICTURES_GALLERYPICTURE_CSS_CLASSES',
    defaults.CSS_CLASSES
)
GALLERYPICTURE_HEIGHTS = getattr(
    settings,
    'PICTURES_GALLERYPICTURE_HEIGHTS',
    defaults.HEIGHTS
)
GALLERYPICTURE_WIDTHS = getattr(
    settings,
    'PICTURES_GALLERYPICTURE_WIDTHS',
    defaults.WIDTHS
)
GALLERYPICTURE_FIELDSETS = getattr(
    settings,
    'PICTURES_GALLERYPICTURE_FIELDSETS',
    (
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': [
                'image',
                'name',
                # 'abstract',
                # 'description',
            ],
        }),
        # (_('settings'), {
        #     'classes': ['section', 'settings'],
        #     'fields': [
        #         'width',
        #         'height',
        #         'css_class',
        #     ],
        # }),
    )
)


PICTURE_CSS_CLASSES = getattr(
    settings,
    'PICTURES_PICTURE_CSS_CLASSES',
    defaults.CSS_CLASSES
)
PICTURE_HEIGHTS = getattr(
    settings,
    'PICTURES_PICTURE_HEIGHTS',
    defaults.HEIGHTS
)
PICTURE_WIDTHS = getattr(
    settings,
    'PICTURES_PICTURE_WIDTHS',
    defaults.WIDTHS
)
PICTURE_FIELDSETS = getattr(
    settings,
    'PICTURES_PICTURE_FIELDSETS',
    (
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': [
                'image',
                'name',
                'abstract',
                'description'
            ],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                'width',
                'height',
                'is_visible',
                'show_popup',
                'css_class',
            ],
        }),
    )
)
