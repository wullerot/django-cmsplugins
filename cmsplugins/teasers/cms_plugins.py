from __future__ import unicode_literals

from django import forms
from django.apps import apps
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import conf
from .models import TeaserWrap, Teaser


class TeaserWrapPluginForm(forms.ModelForm):

    class Meta:
        model = TeaserWrap
        fields = '__all__'
        widgets = {
            'css_class': forms.Select(
                choices=conf.WRAP_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.WRAP_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.WRAP_WIDTHS,
            )
        }


class TeaserWrapPlugin(CMSPluginBase):
    allow_children = conf.WRAP_ALLOW_CHILDREN
    child_classes = conf.WRAP_PLUGINS
    fieldsets = conf.WRAP_FIELDSETS
    form = TeaserWrapPluginForm
    model = TeaserWrap
    name = _('Teasers wrap')
    module = _('content')
    render_template = 'cms/plugins/cms_panels_multipanel.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(TeaserWrapPlugin)


if conf.TEASER_LINK_MODEL:
    class TeaserLinkInline(admin.StackedInline):
        extra = 1
        max_num = 1
        model = apps.get_model(conf.TEASER_LINK_MODEL)
        fields = conf.TEASER_LINK_FIELDS


class TeaserPluginForm(forms.ModelForm):

    class Meta:
        model = Teaser
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 5},
            ),
        }


class TeaserPlugin(CMSPluginBase):
    allow_children = conf.TEASER_ALLOW_CHILDREN
    child_classes = conf.TEASER_PLUGINS
    form = TeaserPluginForm
    fieldsets = conf.TEASER_FIELDSETS
    model = Teaser
    module = _('content')
    name = _('Teaser info')
    if conf.TEASER_LINK_MODEL:
        inlines = [
            TeaserLinkInline
        ]

    render_template = 'cms/plugins/cms_teasers_teaser.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(TeaserPlugin)
