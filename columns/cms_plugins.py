from __future__ import unicode_literals

from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from sections.cms_plugins import WrapPluginForm, WrapPlugin
from sections.models import Wrap
from baseplugin.utils import get_indicator_hidden

from . import conf
from .models import Column


class ColumnPluginForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = conf.COLUMN_FIELDS
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
            'width': forms.RadioSelect(
                choices=conf.WRAP_WIDTHS
            ),
        }


class ColumnPlugin(CMSPluginBase):
    allow_children = True
    child_classes = conf.COLUMN_PLUGINS
    exclude = conf.COLUMN_EXCLUDE
    fieldsets = conf.COLUMN_FIELDSETS
    form = ColumnPluginForm
    model = Column
    module = _('layout')
    name = _('column')
    render_template = 'cms/plugins/columns_column.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder':placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context

plugin_pool.register_plugin(ColumnPlugin)
