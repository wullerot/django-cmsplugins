from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugins import defaults


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

IFRAMEPLUGIN_CONF = {
    'allow_children': False,
    'child_classes': [],
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
        ('Iframe', {
            'classes': [
                'section',
                'iframe'
            ],
            'fields': [
                'markup',
            ],
        }),

    ),
    'required_fields': [],
    'widgets': {
        'bg_color': {
            'widget': 'Select',
            'choices': settings.CMSPLUGINS['defaults']['bg_colors'],
        },
        'css_class': {
            'widget': 'Select',
            'choices': settings.CMSPLUGINS['defaults']['css_classes'],
        },
        'height': {
            'widget': 'Select',
            'choices': settings.CMSPLUGINS['defaults']['heights'],
        },
        'width': {
            'widget': 'Select',
            'choices': settings.CMSPLUGINS['defaults']['widths'],
        },
    }
}

IFRAMEPLUGIN_CONF.update(settings.CMSPLUGINS.get('IFramePlugin', {}))
settings.CMSPLUGINS['IFramePlugin'] = IFRAMEPLUGIN_CONF
