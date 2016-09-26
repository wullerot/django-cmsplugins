from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from baseplugin import defaults


HEADER_CSS_CLASSES = getattr(
    settings,
    'HEADERS_HEADER_CSS_CLASSES',
    defaults.CSS_CLASSES
)
HEADER_EXCLUDE = getattr(
    settings,
    'HEADERS_HEADER_EXCLUDE',
    []
)
HEADER_FIELDS = getattr(
    settings,
    'HEADERS_HEADER_FIELDS',
    '__all__'
)
HEADER_FIELDSETS = getattr(
    settings,
    'HEADERS_HEADER_FIELDSETS',
    (
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': ['name', 'abstract', 'description', 'image'],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': ['width', 'height', 'text_position', 'text_color'],
        }),
        (_('advanced settings'), {
            'classes': ['section', 'settings-advanced'],
            'fields': ['is_visible', 'in_navigation', 'css_class'],
        }),
    )
)
HEADER_HEIGHTS = getattr(
    settings,
    'HEADERS_HEADER_HEIGHTS',
    defaults.HEIGHTS
)
HEADER_WIDTHS = getattr(
    settings,
    'HEADERS_HEADER_WIDTHS',
    defaults.WIDTHS
)
HEADER_TEXT_COLORS = getattr(
    settings,
    'HEADERS_HEADER_TEXT_COLORS',
    defaults.TEXT_COLORS
)
HEADER_TEXT_POSITIONS = getattr(
    settings,
    'HEADERS_HEADER_TEXT_POSITIONS',
    defaults.TEXT_POSITIONS
)
