from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from baseplugin import defaults


VIDEO_CSS_CLASSES = getattr(
    settings,
    'VIDEOS_VIDEO_CSS_CLASSES',
    defaults.CSS_CLASSES
)
VIDEO_HEIGHTS = getattr(
    settings,
    'VIDEOS_VIDEO_HEIGHTS',
    defaults.HEIGHTS
)
VIDEO_WIDTHS = getattr(
    settings,
    'VIDEOS_VIDEO_WIDTHS',
    defaults.WIDTHS
)
VIDEO_EXCLUDE = getattr(
    settings,
    'VIDEOS_VIDEO_EXCLUDE',
    []
)
VIDEO_FIELDS = getattr(
    settings,
    'VIDEOS_VIDEO_FIELDS',
    '__all__'
)
VIDEO_FIELDSETS = getattr(
    settings,
    'VIDEOS_VIDEO_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section', 'content'],
            'fields': [
                'name',
                'video_url',
                'image',
                'abstract',
                'description',
            ],
        }),
        (_('settings'), {
            'classes': ['section', 'settings'],
            'fields': [
                # 'width',
                'height',
                'autoplay',
                'controls',
                'fullscreen',
                'infos',
                'loop',
                'mute',
            ],
        }),
        (_('advanced settings'), {
            'classes': ['section', 'settings-advanced'],
            'fields': [
                'show_name',
                'is_visible',
                'in_navigation',
                'css_class'
            ],
        }),
    ]
)

VIDEOS_RE_RULES = getattr(
    settings,
    'VIDEOS_RE_RULES',
    [
        r"^https?\:\/\/(www\.)?youtu\.be\/(?P<youtube_id>[^\/]*)\??.*$",
        r"^https?\:\/\/(www\.)?youtube\.(com|nl|ru).*v=(?P<youtube_id>.*)\&?.*$",
        r"^https?\:\/\/(www\.)?youtube\.(com|nl|ru)\/embed\/(?P<youtube_id>[^\/]*)\??.*$",
        r"^https?\:\/\/(www\.)?vimeo\.com\/(?P<vimeo_id>[^\/]*)\??.*$",
    ]
)
VIDEOS_DOMAINS = getattr(
    settings,
    'VIDEOS_DOMAINS',
    {
        'youtube': 'https://www.youtube.com/',
        'vimeo': 'https://player.vimeo.com/',
    }
)
