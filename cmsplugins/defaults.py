from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DEFAULTS = {
    'link_model': 'base.models.BaseLink',
    'bg_colors': [
        ('', _('---')),
        ('bg-bright', _('bright')),
        ('bg-dark', _('dark')),
    ],
    'css_classes': [
        ('', _('---')),
    ],
    'heights': [
        ('', _('defined by css')),
        ('window-height h-100', _('full window height')),
        ('window-height h-75', _('75% of window height')),
        ('window-height h-50', _('50% of window height')),
        ('window-height h-25', _('25% of window height')),
        ('ratio ratio-16-9', _('aspect ratio 16:9')),
        ('ratio ratio-2-1', _('aspect ratio 2:1')),
        ('ratio ratio-4-1', _('aspect ratio 4:1')),
    ],
    'widths': [
        ('', _('defined by css')),
        ('w-100', _('100%')),
        ('w-66', _('66%')),
        ('w-50', _('50%')),
        ('w-33', _('33%')),
    ],
    'text_colors': [
        ('', _('---')),
        ('text-bright', _('bright')),
        ('text-dark', _('dark')),
    ],
    'text_positions': [
        ('text-top-left', _('top left')),
        ('text-top-center', _('top center')),
        ('text-top-right', _('top right')),
        ('text-middle-left', _('middle left')),
        ('text-middle-center', _('middle center')),
        ('text-middle-right', _('middle right')),
        ('text-bottom-center', _('bottom center')),
        ('text-bottom-left', _('bottom left')),
        ('text-bottom-right', _('bottom right')),
    ]
}


if not hasattr(settings, 'CMSPLUGINS'):
    settings.CMSPLUGINS = {}
DEFAULTS.update(settings.CMSPLUGINS.get('defaults', {}))
settings.CMSPLUGINS['defaults'] = DEFAULTS


LINK_MODEL = settings.CMSPLUGINS['defaults']['link_model']
BACKGROUND_COLORS = settings.CMSPLUGINS['defaults']['bg_colors']
CSS_CLASSES = settings.CMSPLUGINS['defaults']['css_classes']
HEIGHTS = settings.CMSPLUGINS['defaults']['heights']
WIDTHS = settings.CMSPLUGINS['defaults']['widths']
TEXT_COLORS = settings.CMSPLUGINS['defaults']['text_colors']
TEXT_POSITIONS = settings.CMSPLUGINS['defaults']['text_positions']
