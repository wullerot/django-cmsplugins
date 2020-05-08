from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugins.mixins import CMSPluginMixin, CMSPluginFormMixin
from cmsplugins.utils import get_indicator_hidden

from .models import IFrame


class IFramePluginForm(CMSPluginFormMixin, forms.ModelForm):

    class Meta:
        model = IFrame
        fields = '__all__'


class IFramePlugin(CMSPluginMixin, CMSPluginBase):

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
