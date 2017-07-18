from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


TEASERSWRAP_ALLOW_CHILDREN = getattr(
    settings,
    'TEASERS_TEASERSWRAP_ALLOW_CHILDREN',
    True
)
TEASERSWRAP_PLUGINS = getattr(
    settings,
    'TEASERS_TEASERSWRAP_PLUGINS',
    [
        'TeaserPlugin',
    ]
)
TEASERSWRAP_FIELDSETS = getattr(
    settings,
    'TEASERS_TEASERSWRAP_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section'],
            'fields': [
                'name',
            ],
        }),
        (_('settings'), {
            'classes': [
                'section',
                'collapse',
            ],
            'fields': [
                'css_class',
                'width',
            ],
        }),
    ]
)
TEASERSWRAP_CSS_CLASSES = getattr(
    settings,
    'TEASERS_TEASERSWRAP_CSS_CLASSES',
    [
        ('', _('None')),
    ]
)
TEASERSWRAP_HEIGHTS = getattr(
    settings,
    'TEASERS_TEASERSWRAP_HEIGHTS',
    [
        ('', _('auto')),
    ]
)
TEASERSWRAP_WIDTHS = getattr(
    settings,
    'TEASERS_TEASERSWRAP_WIDTHS',
    [
        ('', _('auto')),
    ]
)


TEASER_FIELDSETS = getattr(
    settings,
    'TEASERS_TEASER_FIELDSETS',
    [
        (_('Page (auto content)'), {
            'classes': ['section'],
            'fields': [
                'link_cms',
            ],
        }),
        (_('Content'), {
            'classes': ['section'],
            'fields': [
                'name',
                'body',
                'filer_image',
                'filer_icon',
            ],
        }),
    ]
)
TEASER_ALLOW_CHILDREN = getattr(
    settings,
    'TEASERS_TEASER_ALLOW_CHILDREN',
    False
)
TEASER_PLUGINS = getattr(
    settings,
    'TEASERS_TEASER_PLUGINS',
    []
)
TEASER_LINK_MODEL = getattr(
    settings,
    'TEASERS_TEASER_LINK_MODEL',
    None
)
TEASER_LINK_FIELDS = getattr(
    settings,
    'TEASERS_TEASER_LINK_FIELDS',
    None
)
TEASER_PAGE_INFO_MODELS = getattr(
    settings,
    'TEASERS_TEASER_PAGE_INFO_MODELS',
    None
)
