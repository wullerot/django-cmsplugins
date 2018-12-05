from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugins.base import defaults

if not hasattr(settings, 'CMSPLUGINS'):
    settings.CMSPLUGINS = {}

"""
'css_class': {
    'widget': 'Select',
    'choices': defaults.CSS_CLASSES,
},
'height': {
    'widget': 'Select',
    'choices': defaults.HEIGHTS,
},
'width': {
    'widget': 'Select',
    'choices': defaults.WIDTHS,
},
"""

if not settings.CMSPLUGINS.get('ColumnPlugin'):
    settings.CMSPLUGINS['ColumnPlugin'] = {
        'widgets': {
            'bg_color': {
                'widget': 'django.forms.Select',
                'choices': defaults.BACKGROUND_COLORS,
                'attrs': {'class': 'huibu'},
            },

        },
        'fieldsets': (
            ('settings', {
                'classes': [
                    'section',
                    'settings'
                ],
                'fields': [
                    'is_visible',
                    'in_navigation',
                ],
            }),
            ('style', {
                'classes': [
                    'section',
                    'style'
                ],
                'fields': [
                    'bg_color',
                    'css_class',
                    'width',
                    'height',
                ],
            }),
            ('title', {
                'classes': [
                    'section',
                    'title'
                ],
                'fields': [
                    'name',
                    'show_name',
                ],
            }),

        ),
        'required_fields': [],
        'plugins': []
    }

# OLD Conf -------------------------------------------------------------------
COLUMN_BACKGROUND_COLORS = getattr(
    settings,
    'COLUMNS_COLUMN_BACKGROUND_COLORS',
    defaults.BACKGROUND_COLORS
)
COLUMN_CSS_CLASSES = getattr(
    settings,
    'COLUMNS_COLUMN_CSS_CLASSES',
    defaults.CSS_CLASSES
)
COLUMN_HEIGHTS = getattr(
    settings,
    'COLUMNS_COLUMN_HEIGHTS',
    defaults.HEIGHTS
)
COLUMN_WIDTHS = getattr(
    settings,
    'COLUMNS_COLUMN_WIDTHS',
    defaults.WIDTHS
)
COLUMN_FIELDSETS = getattr(
    settings,
    'COLUMNS_COLUMN_FIELDSETS',
    (
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                'width',
                'css_class',
            ],
        }),
    )
)
COLUMN_PLUGINS = getattr(
    settings,
    'COLUMNS_COLUMN_PLUGINS',
    []
)
