from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


WRAP_ALLOW_CHILDREN = getattr(
    settings,
    'CMS_TEASERS_WRAP_ALLOW_CHILDREN',
    True
)
WRAP_PLUGINS = getattr(
    settings,
    'CMS_TEASERS_WRAP_PLUGINS',
    [
        'TeaserPlugin',
    ]
)
WRAP_FIELDSETS = getattr(
    settings,
    'CMS_TEASERS_WRAP_FIELDSETS',
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
WRAP_CSS_CLASSES = getattr(
    settings,
    'CMS_TEASERS_WRAP_CSS_CLASSES',
    [
        ('', _('None')),
    ]
)
WRAP_HEIGHTS = getattr(
    settings,
    'CMS_TEASERS_WRAP_HEIGHTS',
    [
        ('', _('auto')),
    ]
)
WRAP_WIDTHS = getattr(
    settings,
    'CMS_TEASERS_WRAP_WIDTHS',
    [
        ('', _('auto')),
    ]
)


TEASER_FIELDSETS = getattr(
    settings,
    'CMS_TEASERS_TEASER_FIELDSETS',
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
    'CMS_TEASERS_TEASER_ALLOW_CHILDREN',
    True
)
TEASER_PLUGINS = getattr(
    settings,
    'CMS_TEASERS_TEASER_PLUGINS',
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
    'TEASERS_TEASER_PAGE_INFO_PLUGINS',
    None
)
