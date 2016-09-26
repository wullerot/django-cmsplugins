from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from baseplugin import defaults


SLIDER_CSS_CLASSES = getattr(
    settings,
    'SLIDERS_SLIDER_CSS_CLASSES',
    defaults.CSS_CLASSES
)
SLIDER_HEIGHTS = getattr(
    settings,
    'SLIDERS_SLIDER_HEIGHTS',
    defaults.HEIGHTS
)
SLIDER_WIDTHS = getattr(
    settings,
    'SLIDERS_SLIDER_WIDTHS',
    defaults.WIDTHS
)

SLIDER_EXCLUDE = getattr(
    settings,
    'SLIDERS_SLIDER_EXCLUDE',
    []
)
SLIDER_FIELDS = getattr(
    settings,
    'SLIDERS_SLIDER_FIELDS',
    '__all__'
)
SLIDER_FIELDSETS = getattr(
    settings,
    'SLIDERS_SLIDER_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': ['name'],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                'show_name',
                'height',
                'autoplay',
                'arrows',
                'indicators',
            ],
        }),
        (_('advanced settings'), {
            'classes': ['section', 'settings-advanced'],
            'fields': ['is_visible', 'in_navigation', 'css_class'],
        }),
    ]
)
SLIDER_PLUGINS = getattr(
    settings,
    'SLIDERS_SLIDER_PLUGINS',
    ['SliderSlidePlugin']
)


SLIDERSLIDE_CSS_CLASSES = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_CSS_CLASSES',
    defaults.CSS_CLASSES
)
SLIDERSLIDE_HEIGHTS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_HEIGHTS',
    defaults.HEIGHTS
)
SLIDERSLIDE_WIDTHS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_WIDTHS',
    defaults.WIDTHS
)
SLIDERSLIDE_EXCLUDE = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_EXCLUDE',
    []
)
SLIDERSLIDE_FIELDS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_FIELDS',
    '__all__'
)
SLIDERSLIDE_FIELDSETS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_FIELDSETS',
    [
        (_('image'), {
            'classes': ['section', 'image'],
            'fields': [
                'image',
                # 'image_animation', # TODO implement
            ],
        }),
        (_('text'), {
            'classes': ['section', 'content'],
            'fields': [
                'name',
                'abstract',
                'description',
                'text_color',
                'text_position',
                # 'text_animation', # TODO implement
            ],
        }),

        (_('advanced settings'), {
            'classes': ['section', 'settings'],
            'fields': ['is_visible', 'css_class'],
        }),
    ]
)
# TODO implement
SLIDERSLIDE_IMAGE_ANIMATIONS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_IMAGE_ANIMATIONS',
    (
        ('', _('---')),
        ('fade_in', _('fade in')),
        ('bottom_up', _('buttom up')),
        ('left_to_right', _('left to right')),
        ('right_to_left', _('right to left')),
        ('top_down', _('top down')),
    )
)
# TODO implement
SLIDERSLIDE_TEXT_ANIMATIONS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_TEXT_ANIMATIONS',
    (
        ('', _('---')),
        ('left_to_right', _('left to right')),
        ('right_to_left', _('right to left')),
        ('fade_in', _('fade in')),
    )
)
SLIDERSLIDE_TEXT_COLORS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_TEXT_COLORS',
    (
        ('', _('defined by css')),
        ('tex-bright', _('bright')),
        ('text-dark', _('dark')),
    )
)
SLIDERSLIDE_TEXT_POSITIONS = getattr(
    settings,
    'SLIDERS_SLIDERSLIDE_TEXT_POSITIONS',
    (
        ('', _('---')),
        ('text-top-left', _('top left')),
        ('text-top-center', _('top center')),
        ('text-top-right', _('top right')),
        ('text-middle-left', _('middle left')),
        ('text-middle-center', _('middle center')),
        ('text-middle-right', _('middle right')),
        ('text-bottom-left', _('bottom left')),
        ('text-bottom-center', _('bottom center')),
        ('text-bottom-right', _('bottom right')),
    )
)
