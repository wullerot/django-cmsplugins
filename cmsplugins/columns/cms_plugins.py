from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugins.base.forms import CMSPluginForm
from cmsplugins.base.utils import get_indicator_hidden
from cmsplugins.base.cms_plugins import CMSPluginMixin

from . import conf
from .models import Column


class ColumnPluginForm(CMSPluginForm):

    class Meta:
        model = Column
        fields = '__all__'


class ColumnPlugin(CMSPluginMixin, CMSPluginBase):
    allow_children = conf.settings.CMSPLUGINS['ColumnPlugin']['allow_children']
    child_classes = conf.settings.CMSPLUGINS['ColumnPlugin']['child_classes']
    fieldsets = conf.settings.CMSPLUGINS['ColumnPlugin']['fieldsets']
    form = ColumnPluginForm
    model = Column
    module = _('layout')
    name = _('column')
    render_template = 'cms/plugins/columns_column.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context


plugin_pool.register_plugin(ColumnPlugin)
