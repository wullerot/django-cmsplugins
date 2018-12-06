from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugins import defaults


CKEDITOR_CSS_CLASSES = getattr(
    settings,
    'TEXT_CKEDITOR_CSS_CLASSES',
    defaults.CSS_CLASSES
)
CKEDITOR_HEIGHTS = getattr(
    settings,
    'TEXT_CKEDITOR_HEIGHTS',
    defaults.HEIGHTS
)
CKEDITOR_WIDTHS = getattr(
    settings,
    'TEXT_CKEDITOR_WIDTHS',
    defaults.WIDTHS
)
CKEDITOR_FIELDSETS = getattr(
    settings,
    'TEXT_CKEDITOR_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section'],
            'fields': ['body'],
        }),
        (_('settings'), {
            'classes': [
                'section',
                'collapse',
            ],
            'fields': [
                'css_class',
                'width',
            ],
        }),
    ]
)
CKEDITOR_ALLOW_CHILDREN = getattr(
    settings,
    'TEXT_CKEDITOR_ALLOW_CHILDREN',
    False
)
CKEDITOR_PLUGINS = getattr(
    settings,
    'TEXT_CKEDITOR_PLUGINS',
    None
)


TEXT_CSS_CLASSES = getattr(
    settings,
    'TEXT_TEXT_CSS_CLASSES',
    defaults.CSS_CLASSES
)
TEXT_HEIGHTS = getattr(
    settings,
    'TEXT_TEXT_HEIGHTS',
    defaults.HEIGHTS
)
TEXT_WIDTHS = getattr(
    settings,
    'TEXT_TEXT_WIDTHS',
    defaults.WIDTHS
)
TEXT_FIELDSETS = getattr(
    settings,
    'TEXT_TEXT_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section'],
            'fields': ['body'],
        }),
        (_('settings'), {
            'classes': [
                'section',
                'collapse',
            ],
            'fields': [
                'css_class',
                'width',
            ],
        }),
    ]
)
TEXT_ALLOW_CHILDREN = getattr(
    settings,
    'TEXT_TEXT_ALLOW_CHILDREN',
    False
)
TEXT_PLUGINS = getattr(
    settings,
    'TEXT_TEXT_PLUGINS',
    None
)


TITLE_CSS_CLASSES = getattr(
    settings,
    'TEXT_TITLE_CSS_CLASSES',
    defaults.CSS_CLASSES
)
TITLE_HEIGHTS = getattr(
    settings,
    'TEXT_TITLE_HEIGHTS',
    defaults.HEIGHTS
)
TITLE_WIDTHS = getattr(
    settings,
    'TEXT_TITLE_WIDTHS',
    defaults.WIDTHS
)
TITLE_FIELDSETS = getattr(
    settings,
    'TEXT_TITLE_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section'],
            'fields': ['body'],
        }),
        (_('settings'), {
            'classes': [
                'section',
                'collapse',
            ],
            'fields': [
                'css_class',
                'width',
            ],
        }),
    ]
)
TITLE_ALLOW_CHILDREN = getattr(
    settings,
    'TEXT_TITLE_ALLOW_CHILDREN',
    False
)
TITLE_PLUGINS = getattr(
    settings,
    'TEXT_TITLE_PLUGINS',
    None
)
