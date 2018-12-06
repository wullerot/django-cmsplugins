from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugins.mixins import CMSPluginMixin, CMSPluginFormMixin
from cmsplugins.utils import get_indicator_hidden

from . import conf
from .models import Section


class SectionPluginForm(CMSPluginFormMixin, forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Section
        widgets = {
            'bg_color': forms.Select(
                choices=conf.SECTION_BACKGROUND_COLORS
            ),
            'css_class': forms.Select(
                choices=conf.SECTION_CSS_CLASSES
            ),
            'height': forms.Select(
                choices=conf.SECTION_HEIGHTS
            ),
            'html_tag': forms.Select(
                choices=conf.SECTION_HTML_TAGS
            ),
            'width': forms.Select(
                choices=conf.SECTION_WIDTHS
            ),
        }


class SectionPlugin(CMSPluginMixin, CMSPluginBase):

    allow_children = True
    child_classes = conf.SECTION_PLUGINS
    fieldsets = conf.SECTION_FIELDSETS
    form = SectionPluginForm
    model = Section
    module = _('layout')
    name = _('Section')
    readonly_fields = [
        'get_absolute_url',
        'get_anchor',
    ]
    render_template = 'cms/plugins/sections_section.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance)
        })
        return context


plugin_pool.register_plugin(SectionPlugin)
