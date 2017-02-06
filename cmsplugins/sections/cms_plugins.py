from __future__ import unicode_literals

from django import forms
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.utils import get_indicator_hidden
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import conf
from .models import Wrap


class WrapPluginForm(forms.ModelForm):
    class Meta:
        fields = conf.WRAP_FIELDS
        model = Wrap
        widgets = {
            'bg_color': forms.Select(
                choices=conf.WRAP_BACKGROUND_COLORS
            ),
            'css_class': forms.Select(
                choices=conf.WRAP_CSS_CLASSES
            ),
            'height': forms.Select(
                choices=conf.WRAP_HEIGHTS
            ),
            'html_tag': forms.RadioSelect(
                choices=conf.WRAP_HTML_TAGS
            ),
            'width': forms.Select(
                choices=conf.WRAP_WIDTHS
            ),
        }


class WrapPlugin(CMSPluginBase):
    allow_children = True
    child_classes = conf.WRAP_PLUGINS
    exclude = conf.WRAP_EXCLUDE
    fieldsets = conf.WRAP_FIELDSETS
    form = WrapPluginForm
    model = Wrap
    module = _('layout')
    name = _('section')
    render_template = 'cms/plugins/sections_wrap.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance)
        })
        return context

plugin_pool.register_plugin(WrapPlugin)
