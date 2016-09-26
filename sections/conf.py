from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from baseplugin import defaults


WRAP_BACKGROUND_COLORS = getattr(
    settings,
    'SECTIONS_WRAP_BACKGROUND_COLORS',
    defaults.BACKGROUND_COLORS
)
WRAP_CSS_CLASSES = getattr(
    settings,
    'SECTIONS_WRAP_CSS_CLASSES',
    defaults.CSS_CLASSES
)
WRAP_HEIGHTS = getattr(
    settings,
    'SECTIONS_WRAP_HEIGHTS',
    defaults.HEIGHTS
)
WRAP_WIDTHS = getattr(
    settings,
    'SECTIONS_WRAP_WIDTHS',
    defaults.WIDTHS
)
WRAP_EXCLUDE = getattr(
    settings,
    'SECTIONS_WRAP_EXCLUDE',
    []
)
WRAP_FIELDS = getattr(
    settings,
    'SECTIONS_WRAP_FIELDS',
    '__all__'
)
WRAP_FIELDSETS = getattr(
    settings,
    'SECTIONS_WRAP_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': [
                'name'
                # 'show_name',
            ],
        }),
        (_('design'), {
            'classes': ['section', 'styles'],
            'fields': [
                # 'width',
                # 'height',
                'bg_color',
                'bg_image',
                'css_class'
            ],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                'is_visible',
                'in_navigation',
                'html_tag',
            ],
        }),
    ]
)
WRAP_HTML_TAGS = getattr(
    settings,
    'SECTIONS_WRAP_HTML_TAGS',
    [
        ('div', _('div')),
        ('article', _('article (if this section could be a page of its own)')),
        ('section', _('section (if this section has a title)')),
    ]
)
WRAP_PLUGINS = getattr(
    settings,
    'SECTIONS_WRAP_PLUGINS',
    []
)
