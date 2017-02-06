from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin import defaults


IFRAME_CSS_CLASSES = getattr(
    settings,
    'IFRAMES_IFRAME_CSS_CLASSES',
    defaults.CSS_CLASSES
)
IFRAME_HEIGHTS = getattr(
    settings,
    'IFRAMES_IFRAME_HEIGHTS',
    defaults.HEIGHTS
)
IFRAME_WIDTHS = getattr(
    settings,
    'IFRAMES_IFRAME_WIDTHS',
    defaults.WIDTHS
)
IFRAME_FIELDSETS = getattr(
    settings,
    'IFRAMES_IFRAME_FIELDSETS',
    (
        (_('content'), {
            'classes': ['section', 'content-text'],
            'fields': ['name', 'markup'],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': ['width', 'height'],
        }),
        (_('advanced settings'), {
            'classes': ['section', 'settings-advanced'],
            'fields': ['is_visible', 'in_navigation', 'css_class'],
        }),
    )
)
