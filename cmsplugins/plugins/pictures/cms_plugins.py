from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugins.mixins import CMSPluginMixin, CMSPluginFormMixin
from cmsplugins.utils import get_indicator_hidden

from . import conf
from .models import Picture, Gallery


class GalleryPluginForm(CMSPluginFormMixin, forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Gallery
        widgets = {
            'abstract': forms.Textarea(
                attrs={'class': 'abstract', 'rows': 2}
            ),
            'css_class': forms.Select(
                choices=conf.GALLERY_CSS_CLASSES,
            ),
            'description': forms.Textarea(
                attrs={'class': 'description', 'rows': 6}
            ),
            'height': forms.Select(
                choices=conf.GALLERY_HEIGHTS,
            ),
            'layout': forms.Select(
                choices=conf.GALLERY_LAYOUTS,
            ),
            'name': forms.TextInput(),
            'width': forms.Select(
                choices=conf.GALLERY_WIDTHS,
            ),
        }


class GalleryPlugin(CMSPluginMixin, CMSPluginBase):
    allow_children = True
    child_classes = conf.GALLERY_PLUGINS
    fieldsets = conf.GALLERY_FIELDSETS
    form = GalleryPluginForm
    model = Gallery
    module = _('content')
    name = _('gallery')
    render_template = 'cms/plugins/pictures_gallery.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context


plugin_pool.register_plugin(GalleryPlugin)


class GalleryPicturePluginForm(CMSPluginFormMixin, forms.ModelForm):
    # TODO check if name is empty
    class Meta:
        fields = '__all__'
        model = Picture
        widgets = {
            'abstract': forms.Textarea(
                attrs={'class': 'abstract', 'rows': 2}
            ),
            'css_class': forms.Select(
                choices=conf.GALLERYPICTURE_CSS_CLASSES,
            ),
            'description': forms.Textarea(
                attrs={'class': 'description', 'rows': 6}
            ),
            'height': forms.Select(
                choices=conf.GALLERYPICTURE_HEIGHTS,
            ),
            'name': forms.TextInput(),
            'width': forms.Select(
                choices=conf.GALLERYPICTURE_WIDTHS,
            ),
        }


class GalleryPicturePlugin(CMSPluginMixin, CMSPluginBase):
    fieldsets = conf.GALLERYPICTURE_FIELDSETS
    form = GalleryPicturePluginForm
    model = Picture
    module = _('content')
    name = _('image')
    render_template = 'cms/plugins/pictures_gallerypicture.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context


plugin_pool.register_plugin(GalleryPicturePlugin)


class PicturePluginForm(CMSPluginFormMixin, forms.ModelForm):
    # TODO check if name is empty
    class Meta:
        fields = '__all__'
        model = Picture
        widgets = {
            'abstract': forms.Textarea(
                attrs={'class': 'abstract', 'rows': 2}
            ),
            'css_class': forms.Select(
                choices=conf.PICTURE_CSS_CLASSES,
            ),
            'description': forms.Textarea(
                attrs={'class': 'description', 'rows': 6}
            ),
            'height': forms.Select(
                choices=conf.PICTURE_HEIGHTS,
            ),
            'name': forms.TextInput(),
            'width': forms.Select(
                choices=conf.PICTURE_WIDTHS,
            ),
        }


class PicturePlugin(CMSPluginMixin, CMSPluginBase):
    fieldsets = conf.PICTURE_FIELDSETS
    form = PicturePluginForm
    model = Picture
    module = _('content')
    name = _('image')
    render_template = 'cms/plugins/pictures_picture.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context


plugin_pool.register_plugin(PicturePlugin)
