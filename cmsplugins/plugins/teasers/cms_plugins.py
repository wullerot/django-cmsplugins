from __future__ import unicode_literals

from django import forms
from django.apps import apps
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugins.mixins import CMSPluginMixin, CMSPluginFormMixin

from . import conf
from .models import TeaserWrap, Teaser


class TeaserWrapPluginForm(CMSPluginFormMixin, forms.ModelForm):

    class Meta:
        model = TeaserWrap
        fields = '__all__'
        widgets = {
            'css_class': forms.Select(
                choices=conf.TEASERSWRAP_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.TEASERSWRAP_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.TEASERSWRAP_WIDTHS,
            )
        }


class TeaserWrapPlugin(CMSPluginMixin, CMSPluginBase):
    allow_children = conf.TEASERSWRAP_ALLOW_CHILDREN
    child_classes = conf.TEASERSWRAP_PLUGINS
    fieldsets = conf.TEASERSWRAP_FIELDSETS
    form = TeaserWrapPluginForm
    model = TeaserWrap
    name = _('Teasers wrap')
    module = _('content')
    render_template = 'cms/plugins/teasers_teaserwrap.html'

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


class TeaserPluginForm(CMSPluginFormMixin, forms.ModelForm):

    class Meta:
        model = Teaser
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 5},
            ),
        }

    def clean(self):
        data = super(TeaserPluginForm, self).clean()
        link_cms = data.get('link_cms', None)
        name = data.get('name', '')
        body = data.get('body', '')
        if not link_cms and not (body or name):
            msg = _('you have to give a name or a text')
            self.add_error('name', msg)
            self.add_error('body', msg)
        return data


class TeaserPlugin(CMSPluginMixin, CMSPluginBase):
    allow_children = conf.TEASER_ALLOW_CHILDREN
    child_classes = conf.TEASER_PLUGINS
    form = TeaserPluginForm
    fieldsets = conf.TEASER_FIELDSETS
    model = Teaser
    module = _('content')
    name = _('Teaser')

    if conf.TEASER_LINK_MODEL:
        inlines = [
            TeaserLinkInline
        ]

    render_template = 'cms/plugins/teasers_teaser.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(TeaserPlugin)
