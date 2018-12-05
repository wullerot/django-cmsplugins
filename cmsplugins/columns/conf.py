from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugins.base import defaults


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
