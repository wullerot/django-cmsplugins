from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.models import BasePlugin
from filer.fields.image import FilerImageField

from .utils import VideoMixin


class Video(VideoMixin, BasePlugin):
    autoplay = models.BooleanField(
        default=False,
        verbose_name=_('auto play'),
    )
    controls = models.BooleanField(
        default=True,
        help_text=_('only youtube'),
        verbose_name=_('show controls'),
    )
    fullscreen = models.BooleanField(
        default=True,
        verbose_name=_('allow fullscreen'),
    )
    infos = models.BooleanField(
        default=True,
        verbose_name=_('show infos'),
    )
    loop = models.BooleanField(
        default=False,
        verbose_name=_('loop'),
    )
    mute = models.BooleanField(
        default=False,
        verbose_name=_('mute'),
    )
    abstract = models.TextField(
        max_length=250,
        blank=True,
        default='',
        verbose_name=_('abstract'),
    )
    description = models.TextField(
        blank=True,
        default='',
        verbose_name=_('description'),
    )
    video_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('video url'),
        help_text=_('youtube & vimeo urls only'),
    )
    image = FilerImageField(
        null=True,
        default=None,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('image'),
        help_text=_('placeholder image'),
    )

    @property
    def data_tags(self):
        # TODO implement js api version
        attrs = ['autoplay', 'controls', 'loop', 'infos', 'mute']
        data = [
            'data-provider="{0}"'.format(self.video_type),
            'data-video_id="{0}"'.format(self.video_id),
            'data-video_url="{0}"'.format(self.video_jsapi_url),
        ]
        for attr in attrs:
            value = str(getattr(self, attr)).lower()
            data.append('data{0}="{1}"'.format(attr, value))
        return mark_safe(' {0}'.format(' '.join(data)))

    def get_video_attrs(self):
        attrs = []
        # Vimeo & Youtube
        if self.autoplay:
            attrs.append('autoplay=1')
        if self.loop:
            attrs.append('loop=1')
        # Vimeo only
        if self._video_type == 'vimeo':
            attrs.append('color=cccccc')
            if self.fullscreen:
                attrs.append('fullscreen=1')
            if not self.infos:
                attrs.append('badge=0')
                attrs.append('byline=0')
                attrs.append('portrait=0')
                attrs.append('title=0')
        # Youtube only
        if self._video_type == 'youtube':
            attrs.append('modestbranding=1')
            attrs.append('rel=0')
            if not self.controls:
                attrs.append('controls=0')
            if not self.fullscreen:
                attrs.append('fs=0')
            if not self.infos:
                attrs.append('showinfo=0')
            if self.loop:
                attrs.append('playlist={0}'.format(self._video_id))
        return '&'.join(attrs)
