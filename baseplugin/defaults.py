from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


LINK_MODEL = getattr(
    settings,
    'BASEPLUGIN_LINK_MODEL',
    'baseplugin.models.BaseLink'
)
CSS_CLASSES = getattr(
    settings,
    'BASEPLUGIN_CSS_CLASSES',
    [
        ('', _('---')),
    ]
)
HEIGHTS = getattr(
    settings,
    'BASEPLUGIN_HEIGHTS',
    (
        ('', _('defined by css')),
        ('window-height h-100', _('full window height')),
        ('window-height h-75', _('75% of window height')),
        ('window-height h-50', _('50% of window height')),
        ('window-height h-25', _('25% of window height')),
        ('ratio ratio-16-9', _('aspect ratio 16:9')),
        ('ratio ratio-2-1', _('aspect ratio 2:1')),
        ('ratio ratio-4-1', _('aspect ratio 4:1')),
    )
)
WIDTHS = getattr(
    settings,
    'BASEPLUGIN_WIDTHS',
    (
        ('', _('defined by css')),
        ('w-100', _('100%')),
        ('w-66', _('66%')),
        ('w-50', _('50%')),
        ('w-33', _('33%')),
    )
)
BACKGROUND_COLORS = getattr(
    settings,
    'BASEPLUGIN_BACKGROUND_COLORS',
    (
        ('', _('---')),
        ('bg-bright', _('bright')),
        ('bg-dark', _('dark')),
    )
)
TEXT_COLORS = getattr(
    settings,
    'BASEPLUGIN_TEXT_COLORS',
    (
        ('', _('---')),
        ('text-bright', _('bright')),
        ('text-dark', _('dark')),
    )
)
TEXT_POSITIONS = getattr(
    settings,
    'BASEPLUGIN_TEXT_POSITIONS',
    (
        ('text-top-left', _('top left')),
        ('text-top-center', _('top center')),
        ('text-top-right', _('top right')),
        ('text-middle-left', _('middle left')),
        ('text-middle-center', _('middle center')),
        ('text-middle-right', _('middle right')),
        ('text-bottom-center', _('bottom center')),
        ('text-bottom-left', _('bottom left')),
        ('text-bottom-right', _('bottom right')),
    )
)
