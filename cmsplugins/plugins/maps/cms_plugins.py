from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugins.forms import CMSPluginForm
from cmsplugins.utils import get_indicator_hidden

from . import conf
from .models import GoogleMap


class GoogleMapPluginForm(CMSPluginForm):

    class Meta:
        fields = '__all__'
        model = GoogleMap
        widgets = {
            'css_class': forms.Select(
                choices=conf.GOOGLEMAP_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.GOOGLEMAP_HEIGHTS,
            ),
            'info_content': forms.Textarea(
                attrs={'rows': 4}
            ),
            'map_type': forms.Select(
                choices=conf.GOOGLEMAP_TYPES,
            ),
            'width': forms.Select(
                choices=conf.GOOGLEMAP_WIDTHS,
            ),
            'zoom': forms.Select(
                choices=conf.GOOGLEMAP_ZOOM_LEVELS,
            ),
        }


class GoogleMapPlugin(CMSPluginBase):
    fieldsets = conf.GOOGLEMAP_FIELDSETS
    form = GoogleMapPluginForm
    model = GoogleMap
    module = _('content')
    name = _("Google Map")
    render_template = "cms/plugins/maps_googlemap.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'indicator_hidden': get_indicator_hidden(request, instance),
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(GoogleMapPlugin)


class StreetViewPluginForm(CMSPluginForm):
    class Meta:
        fields = '__all__'
        model = GoogleMap
        widgets = {
            'css_class': forms.Select(
                choices=conf.STREETVIEW_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.STREETVIEW_HEIGHTS,
            ),
            'info_content': forms.Textarea(
                attrs={'rows': 4}
            ),
            'width': forms.Select(
                choices=conf.STREETVIEW_WIDTHS,
            ),
        }


class StreetViewPlugin(CMSPluginBase):
    fieldsets = conf.STREETVIEW_FIELDSETS
    form = StreetViewPluginForm
    model = GoogleMap
    module = _('content')
    name = _("Google Street View")
    render_template = "cms/plugins/maps_streetview.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'indicator_hidden': get_indicator_hidden(request, instance),
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(StreetViewPlugin)
