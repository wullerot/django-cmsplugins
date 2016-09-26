from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from baseplugin import defaults


if not hasattr(settings, 'MAPS_GOOGLEMAP_BROWSER_KEY'):
    raise ImproperlyConfigured(
        'you have to set MAPS_GOOGLEMAP_BROWSER_KEY to a valid Google Maps'
        ' Browser API Key in your settings file'
    )
if not hasattr(settings, 'MAPS_GOOGLEMAP_SERVER_KEY'):
    raise ImproperlyConfigured(
        'you have to set MAPS_GOOGLEMAP_SERVER_KEY to a valid Google Maps'
        ' Server API Key in your settings file'
    )


GOOGLEMAP_BROWSER_KEY = getattr(
    settings,
    'MAPS_GOOGLEMAP_BROWSER_KEY',
    None
)
GOOGLEMAP_SERVER_KEY = getattr(
    settings,
    'MAPS_GOOGLEMAP_SERVER_KEY',
    None
)


GOOGLEMAP_CSS_CLASSES = getattr(
    settings,
    'MAPS_GOOGLEMAP_CSS_CLASSES',
    defaults.CSS_CLASSES
)
GOOGLEMAP_EXCLUDE = getattr(
    settings,
    'MAPS_GOOGLEMAP_EXCLUDE',
    []
)
GOOGLEMAP_FIELDS = getattr(
    settings,
    'MAPS_GOOGLEMAP_FIELDS',
    '__all__'
)
GOOGLEMAP_FIELDSETS = getattr(
    settings,
    'MAPS_GOOGLEMAP_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': [
                'name',
                'address',
                ('zipcode', 'city'),
                'info_content',
                'info_image',
                ('lat', 'lng'),
            ],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                'width',
                'height',
                'info_window',
                'zoom',
                'map_type',
            ],
        }),
        (_('advanced settings'), {
            'classes': ['section', 'settings-advanced'],
            'fields': [
                # ('route_planer_title', 'route_planer'), not implemented yet
                'scrollwheel',
                'double_click_zoom',
                'draggable',
                'keyboard_shortcuts',
                'pan_control',
                'zoom_control',
                'street_view_control',
                'style'
            ],
        }),
        (_('plugin settings'), {
            'classes': ['collapse', 'content', 'content-advanced'],
            'fields': [
                'show_name',
                'is_visible',
                'in_navigation',
                'css_class',
            ],
        }),
    ]
)
GOOGLEMAP_TYPES = getattr(
    settings,
    'MAPS_GOOGLEMAP_TYPES',
    [
        ('ROADMAP', _('Roadmap: displays a normal street map.')),
        ('HYBRID', _('Hybrid: displays a transparent layer of major streets '
                     'on satellite images.')),
        ('SATELLITE', _('Satellite: displays satellite images.')),
        ('TERRAIN', _('Terrain: displays maps with physical features such as '
                      'terrain and vegetation.')),
    ]
)
GOOGLEMAP_HEIGHTS = getattr(
    settings,
    'MAPS_GOOGLEMAP_HEIGHTS',
    defaults.HEIGHTS
)
GOOGLEMAP_WIDTHS = getattr(
    settings,
    'MAPS_GOOGLEMAP_WIDTHS',
    defaults.WIDTHS
)
GOOGLEMAP_ZOOM_LEVELS = getattr(
    settings,
    'MAPS_GOOGLEMAP_ZOOM_LEVELS',
    map(lambda c: (c, str(c)), range(22))
)


STREETVIEW_CSS_CLASSES = getattr(
    settings,
    'MAPS_STREETVIEW_CSS_CLASSES',
    defaults.CSS_CLASSES
)
STREETVIEW_EXCLUDE = getattr(
    settings,
    'MAPS_STREETVIEW_EXCLUDE',
    []
)
STREETVIEW_FIELDS = getattr(
    settings,
    'MAPS_STREETVIEW_FIELDS',
    '__all__'
)
STREETVIEW_FIELDSETS = getattr(
    settings,
    'MAPS_STREETVIEW_FIELDSETS',
    (
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': [
                'name',
                'address',
                ('zipcode', 'city'),
                ('lat', 'lng'),
            ],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                'width',
                'height',
                ('pan_heading', 'pan_pitch'),
            ],
        }),
        (_('advanced settings'), {
            'classes': ['section', 'settings-advanced'],
            'fields': [
                'scrollwheel',
                'double_click_zoom',
                'draggable',
            ],
        }),
        (_('plugin settings'), {
            'classes': ['section', 'settings-advanced'],
            'fields': [
                'show_name',
                'is_visible',
                'in_navigation',
                'css_class',
            ],
        }),
    )
)
STREETVIEW_HEIGHTS = getattr(
    settings,
    'MAPS_STREETVIEW_HEIGHTS',
    defaults.HEIGHTS
)
STREETVIEW_WIDTHS = getattr(
    settings,
    'MAPS_STREETVIEW_WIDTHS',
    defaults.WIDTHS
)
