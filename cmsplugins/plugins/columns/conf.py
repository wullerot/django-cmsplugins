from __future__ import unicode_literals

from django.conf import settings

from cmsplugins import defaults


if not hasattr(settings, 'CMSPLUGINS'):
    settings.CMSPLUGINS = {}


settings.CMSPLUGINS['ColumnPlugin'] = {
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

    ),
    'required_fields': [],
    'widgets': {
        'bg_color': {
            'widget': 'Select',
            'choices': defaults.BACKGROUND_COLORS,
        },
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
    }

}
