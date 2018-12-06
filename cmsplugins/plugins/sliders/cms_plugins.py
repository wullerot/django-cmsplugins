from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugins.forms import CMSPluginForm
from cmsplugins.utils import get_indicator_hidden, load_object

from . import conf
from .models import Slider, Slide


class SliderLinkInlineForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = load_object(conf.SLIDER_LINK_MODEL)
        widgets = {
            'abstract': forms.Textarea(attrs={'rows': 3})
        }


class SliderLinkInline(admin.StackedInline):
    extra = 1
    max_num = 1
    fields = conf.SLIDER_LINK_FIELDS
    form = SliderLinkInlineForm
    model = load_object(conf.SLIDER_LINK_MODEL)


class SlideLinkInlineForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = load_object(conf.SLIDE_LINK_MODEL)
        widgets = {
            'abstract': forms.Textarea(attrs={'rows': 3})
        }


class SlideLinkInline(admin.StackedInline):
    extra = 1
    max_num = 1
    fields = conf.SLIDE_LINK_FIELDS
    form = SlideLinkInlineForm
    model = load_object(conf.SLIDE_LINK_MODEL)


class SliderPluginForm(CMSPluginForm):
    class Meta:
        model = Slider
        fields = conf.SLIDER_FIELDS
        widgets = {
            'css_class': forms.Select(
                choices=conf.SLIDER_CSS_CLASSES
            ),
            'height': forms.Select(
                choices=conf.SLIDER_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.SLIDER_WIDTHS,
            ),
        }


class SliderPlugin(CMSPluginBase):
    allow_children = True
    child_classes = conf.SLIDER_PLUGINS
    exclude = conf.SLIDER_EXCLUDE
    fieldsets = conf.SLIDER_FIELDSETS
    form = SliderPluginForm
    inlines = [load_object(i) for i in conf.SLIDER_INLINES]
    model = Slider
    module = _('content')
    name = _('slider')
    render_template = 'cms/plugins/sliders_slider.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context


plugin_pool.register_plugin(SliderPlugin)


class SliderSlidePluginForm(CMSPluginForm):
    class Meta:
        model = Slide
        fields = conf.SLIDERSLIDE_FIELDS
        widgets = {
            'abstract': forms.Textarea(
                attrs={'rows': 2},
            ),
            'css_class': forms.Select(
                choices=conf.SLIDERSLIDE_CSS_CLASSES
            ),
            'description': forms.Textarea(
                attrs={'rows': 4}
            ),
            'height': forms.Select(
                choices=conf.SLIDERSLIDE_HEIGHTS,
            ),
            'image_animation': forms.Select(
                choices=conf.SLIDERSLIDE_IMAGE_ANIMATIONS,
            ),
            'name': forms.Textarea(
                attrs={'rows': 2},
            ),
            'name_sub': forms.Textarea(
                attrs={'rows': 2},
            ),
            'text_animation': forms.Select(
                choices=conf.SLIDERSLIDE_TEXT_ANIMATIONS,
            ),
            'text_color': forms.Select(
                choices=conf.SLIDERSLIDE_TEXT_COLORS,
            ),
            'text_position': forms.Select(
                choices=conf.SLIDERSLIDE_TEXT_POSITIONS,
            ),
            'width': forms.Select(
                choices=conf.SLIDERSLIDE_WIDTHS,
            ),
        }


class SliderSlidePlugin(CMSPluginBase):
    allow_children = False
    exclude = conf.SLIDERSLIDE_EXCLUDE
    fieldsets = conf.SLIDERSLIDE_FIELDSETS
    form = SliderSlidePluginForm
    inlines = [load_object(i) for i in conf.SLIDE_INLINES]
    model = Slide
    module = _('content')
    name = _('slide')
    render_template = 'cms/plugins/sliders_sliderslide.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context


plugin_pool.register_plugin(SliderSlidePlugin)
