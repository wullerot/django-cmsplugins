from __future__ import unicode_literals

from django.conf import settings


if not hasattr(settings, 'CMSPLUGINS'):
    settings.CMSPLUGINS = {}


HEADERPLUGIN_CONF = {
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
        ('content', {
            'classes': [
                'section',
                'content'
            ],
            'fields': [
                'abstract',
                'description',
                'text_position',
                'text_color',
                'image'
            ],
        }),

    ),
    'required_fields': [],
    'widgets': {
        'bg_color': {
            'choices': settings.CMSPLUGINS['defaults']['bg_colors'],
        },
        'css_class': {
            'choices': settings.CMSPLUGINS['defaults']['css_classes'],
        },
        'height': {
            'choices': settings.CMSPLUGINS['defaults']['heights'],
        },
        'width': {
            'choices': settings.CMSPLUGINS['defaults']['widths'],
        },
        'text_color': {
            'choices': settings.CMSPLUGINS['defaults']['text_colors'],
        },
        'text_position': {
            'choices': settings.CMSPLUGINS['defaults']['text_positions'],
        },
    }
}


HEADERPLUGIN_CONF.update(settings.CMSPLUGINS.get('HeaderPlugin', {}))
settings.CMSPLUGINS['HeaderPlugin'] = HEADERPLUGIN_CONF
