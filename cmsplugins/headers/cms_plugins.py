from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.utils import get_indicator_hidden
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import conf
from .models import Header


class HeaderPluginForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = '__all__'
        widgets = {
            'abstract': forms.Textarea(
                attrs={'rows': 4}
            ),
            'css_class': forms.Select(
                choices=conf.HEADER_CSS_CLASSES,
            ),
            'description': forms.Textarea(
                attrs={'rows': 8}
            ),
            'height': forms.Select(
                attrs={'class': 'width'},
                choices=conf.HEADER_HEIGHTS,
            ),
            'name': forms.Textarea(
                attrs={'rows': 2}
            ),
            'text_color': forms.Select(
                choices=conf.HEADER_TEXT_COLORS,
            ),
            'text_position': forms.Select(
                choices=conf.HEADER_TEXT_POSITIONS,
            ),
            'width': forms.Select(
                attrs={'class': 'width'},
                choices=conf.HEADER_WIDTHS,
            ),
        }


class HeaderPlugin(CMSPluginBase):
    fieldsets = conf.HEADER_FIELDSETS
    form = HeaderPluginForm
    model = Header
    module = _('content')
    name = _('header')
    render_template = 'cms/plugins/headers_header.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context

plugin_pool.register_plugin(HeaderPlugin)
