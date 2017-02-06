from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from text_ckeditor.widgets import CKEditorWidget

from . import conf
from .models import Text


class TextCKEditorPluginForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Text
        widgets = {
            'body': CKEditorWidget(
                conf={'fullscreen': False}
            ),
            'css_class': forms.Select(
                choices=conf.CKEDITOR_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.CKEDITOR_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.CKEDITOR_WIDTHS,
            ),
        }


class TextCKEditorPlugin(CMSPluginBase):
    fieldsets = conf.CKEDITOR_FIELDSETS
    form = TextCKEditorPluginForm
    model = Text
    module = _('content')
    name = _('text (editor)')
    render_template = 'cms/plugins/text_ckeditor.html'

    def render(self, context, instance, placeholder):
        context.update({'object': instance, 'placeholder': placeholder})
        return context

plugin_pool.register_plugin(TextCKEditorPlugin)


class TextPluginForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Text
        widgets = {
            'body': forms.Textarea(
                attrs={'class': 'text-plain'}
            ),
            'css_class': forms.Select(
                choices=conf.TEXT_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.TEXT_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.TEXT_WIDTHS,
            ),
        }


class TextPlugin(CMSPluginBase):
    fieldsets = conf.TEXT_FIELDSETS
    form = TextPluginForm
    model = Text
    module = _('content')
    name = _('plain text')
    render_template = 'cms/plugins/text_text.html'

    def render(self, context, instance, placeholder):
        context.update({'object': instance, 'placeholder': placeholder})
        return context

plugin_pool.register_plugin(TextPlugin)


class TitlePluginForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Text
        widgets = {
            'body': forms.Textarea(
                attrs={'class': 'text-title', 'rows': 2}
            ),
            'css_class': forms.Select(
                choices=conf.TITLE_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.TITLE_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.TITLE_WIDTHS,
            ),
        }


class TitlePlugin(CMSPluginBase):
    fieldsets = conf.TITLE_FIELDSETS
    form = TitlePluginForm
    model = Text
    module = _('content')
    name = _('title h1')
    render_template = 'cms/plugins/text_title.html'

    def render(self, context, instance, placeholder):
        context.update({'object': instance, 'placeholder': placeholder})
        return context

plugin_pool.register_plugin(TitlePlugin)
