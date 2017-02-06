from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.utils import get_indicator_hidden
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import conf
from .models import IFrame


class IFramePluginForm(forms.ModelForm):
    class Meta:
        model = IFrame
        fields = conf.IFRAME_FIELDS
        widgets = {
            'css_class': forms.Select(
                choices=conf.IFRAME_CSS_CLASSES,
            ),
            'height': forms.RadioSelect(
                attrs={'class': 'width'},
                choices=conf.IFRAME_HEIGHTS,
            ),
            'markup': forms.Textarea(
                attrs={'rows': 10}
            ),
            'name': forms.Textarea(
                attrs={'rows': 2}
            ),
            'width': forms.RadioSelect(
                attrs={'class': 'width'},
                choices=conf.IFRAME_WIDTHS,
            ),
        }


class IFramePlugin(CMSPluginBase):
    exclude = conf.IFRAME_EXCLUDE
    fieldsets = conf.IFRAME_FIELDSETS
    form = IFramePluginForm
    model = IFrame
    module = _('content')
    name = _('iframe')
    render_template = 'cms/plugins/iframes_iframe.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context

plugin_pool.register_plugin(IFramePlugin)
