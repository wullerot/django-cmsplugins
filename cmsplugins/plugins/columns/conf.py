from __future__ import unicode_literals

from django.conf import settings


COLUMNPLUGIN_CONF = {
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


COLUMNPLUGIN_CONF.update(settings.CMSPLUGINS.get('ColumnPlugin', {}))
settings.CMSPLUGINS['ColumnPlugin'] = COLUMNPLUGIN_CONF
