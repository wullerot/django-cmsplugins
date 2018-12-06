from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugins import defaults


SECTION_BACKGROUND_COLORS = getattr(
    settings,
    'SECTIONS_SECTION_BACKGROUND_COLORS',
    defaults.BACKGROUND_COLORS
)
SECTION_CSS_CLASSES = getattr(
    settings,
    'SECTIONS_SECTION_CSS_CLASSES',
    defaults.CSS_CLASSES
)
SECTION_HEIGHTS = getattr(
    settings,
    'SECTIONS_SECTION_HEIGHTS',
    defaults.HEIGHTS
)
SECTION_WIDTHS = getattr(
    settings,
    'SECTIONS_SECTION_WIDTHS',
    defaults.WIDTHS
)
SECTION_FIELDSETS = getattr(
    settings,
    'SECTIONS_SECTION_FIELDSETS',
    [
        (_('Info'), {
            'classes': [
                'section',
            ],
            'fields': [
                'get_absolute_url',
            ],
        }),
        (_('Content'), {
            'classes': [
                'section',
            ],
            'fields': [
                'name',
                'show_name',
            ],
        }),
        (_('Design'), {
            'classes': [
                'section',
            ],
            'fields': [
                'width',
                'height',
                'bg_color',
                'bg_image',
                'css_class'
            ],
        }),
        (_('Settings'), {
            'classes': [
                'section',
            ],
            'fields': [
                'is_visible',
                'in_navigation',
                'html_tag',
            ],
        }),
    ]
)
SECTION_HTML_TAGS = getattr(
    settings,
    'SECTIONS_SECTION_HTML_TAGS',
    [
        ('div', _('div')),
        ('article', _('article (if this section could be a page of its own)')),
        ('section', _('section (if this section has a title)')),
    ]
)
SECTION_PLUGINS = getattr(
    settings,
    'SECTIONS_SECTION_PLUGINS',
    []
)
