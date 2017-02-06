from __future__ import unicode_literals

from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugins.baseplugin.utils import get_indicator_hidden

from . import conf
from .models import Column


class ColumnPluginForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = '__all__'
        widgets = {
            'bg_color': forms.Select(
                choices=conf.COLUMN_BACKGROUND_COLORS
            ),
            'css_class': forms.Select(
                choices=conf.COLUMN_CSS_CLASSES
            ),
            'height': forms.Select(
                choices=conf.COLUMN_HEIGHTS
            ),
            'width': forms.Select(
                choices=conf.COLUMN_WIDTHS
            ),
        }


class ColumnPlugin(CMSPluginBase):
    allow_children = True
    child_classes = conf.COLUMN_PLUGINS
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
