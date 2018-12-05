from __future__ import unicode_literals

import json

from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

import googlemaps
from cmsplugins.base.models import BasePlugin
from filer.fields.image import FilerImageField

from . import conf


class GoogleMap(BasePlugin):
    # TODO log warning on save (googlemaps api)
    # TODO implement route planer
    # TODO simple image & link version
    browser_apikey = conf.GOOGLEMAP_BROWSER_KEY
    server_apikey = conf.GOOGLEMAP_SERVER_KEY

    address = models.CharField(
        max_length=150,
        verbose_name=_('address'),
    )
    zipcode = models.CharField(
        max_length=30,
        verbose_name=_('zip code'),
    )
    city = models.CharField(
        max_length=100,
        verbose_name=_('city'),
    )
    info_content = models.TextField(
        max_length=255,
        blank=True,
        verbose_name=_('textbox content'),
        help_text=_('content help'),
    )
    info_image = FilerImageField(
        null=True,
        default=None,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('textbox image'),
    )
    map_type = models.CharField(
        max_length=40,
        default='ROADMAP',
        verbose_name=_('map type'),
    )
    style = models.TextField(
        blank=True,
        help_text=_('google map styles'),
        verbose_name=_('custom map style'),
    )
    zoom = models.PositiveSmallIntegerField(
        default=14,
        verbose_name=_('zoom level'),
    )
    lat = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_('latitude'),
    )
    lng = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_('longitude'),
        help_text=_('lat help'),
    )
    pan_heading = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_('camera orientation'),
    )
    pan_pitch = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_('camera pitch'),
    )
    route_planer_title = models.CharField(
        null=True,
        max_length=150,
        blank=True,
        default=_('Calculate your fastest way to here'),
        verbose_name=_('route planner title'),
    )
    route_planer = models.BooleanField(
        default=False,
        verbose_name=_('route planner'),
    )
    info_window = models.BooleanField(
        default=True,
        verbose_name=_('info window'),
        help_text=_('Show textbox over marker'),
    )
    scrollwheel = models.BooleanField(
        default=True,
        verbose_name=_('scrollwheel'),
        help_text=_('scrollwheel help'),
    )
    double_click_zoom = models.BooleanField(
        default=True,
        verbose_name=_('double click zoom'),
    )
    draggable = models.BooleanField(
        default=True,
        verbose_name=_('draggable'),
    )
    keyboard_shortcuts = models.BooleanField(
        default=True,
        verbose_name=_('keyboard shortcuts'),
    )
    pan_control = models.BooleanField(
        default=True,
        verbose_name=_('Pan control'),
    )
    zoom_control = models.BooleanField(
        default=True,
        verbose_name=_('zoom control'),
    )
    street_view_control = models.BooleanField(
        default=True,
        verbose_name=_('Street View control'),
    )

    def save(self, *args, **kwargs):
        if not self.lat and not self.lng:
            gmaps = googlemaps.Client(key=self.server_apikey)
            info = self.__dict__
            address = '{name}, {address}, {zipcode} {city}'.format(**info)
            try:
                geocode_result = gmaps.geocode(address)
                self.lat = geocode_result[0]['geometry']['location']['lat']
                self.lng = geocode_result[0]['geometry']['location']['lng']
            except Exception as e:
                pass
        super(GoogleMap, self).save(*args, **kwargs)

    @property
    def data_tags(self):
        data = {
            'data-id': self.pk,
            'data-title': self.name,
            'data-address': '{0}, {1} {2}'.format(
                self.address,
                self.zipcode,
                self.city,
            ),
            'data-street': self.address,
            'data-zip': self.zipcode,
            'data-city': self.city,
            'data-lat': self.lat,
            'data-lng': self.lng,
            'data-double_click_zoom': str(not self.double_click_zoom).lower(),
            'data-scrollwheel': str(self.scrollwheel).lower(),
            'data-zoom_control': str(self.pan_control).lower(),
        }
        if self.plugin_type == 'GoogleMapPlugin':
            data.update({
                'data-zoom': self.zoom,
                'data-draggable': str(self.draggable).lower(),
                'data-keyboard_shortcuts': str(
                    self.keyboard_shortcuts
                ).lower(),
                'data-map_type': self.map_type,
                'data-pan_control': str(self.pan_control).lower(),
                'data-show_infowindow': str(self.info_window).lower(),
                'data-street_view_control': str(
                    self.street_view_control
                ).lower(),
            })
            if self.info_content:
                lines = self.info_content.replace('"', '\'').splitlines()
                lines[0] = '<strong>{0}</strong>'.format(lines[0])
                data['data-info'] = '<br>'.join(lines)
            else:
                info = '<strong>{0}</strong><br>{1}<br>{2} {3}<br>'.format(
                    self.name,
                    self.address,
                    self.zipcode,
                    self.city
                )
                data['data-info'] = mark_safe(info)
            if self.info_image:
                data['data-info_image'] = self.info_image.url
            if self.style:
                style = ''.join(self.style.splitlines())
                style = style.replace(' ', '')
                style = style.replace('"', '\'')
                data['data-style'] = style
        elif self.plugin_type == 'StreetViewPlugin':
            if self.pan_heading:
                data['data-pan_heading'] = self.pan_heading
            if self.pan_pitch:
                data['data-pan_pitch'] = self.pan_pitch
        tags = ' '.join(['{0}="{1}"'.format(k, v) for k, v in data.items()])
        return mark_safe(tags)
