from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.utils import get_indicator_hidden
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import conf
from .models import Video


class VideoPluginForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'abstract': forms.Textarea(
                attrs={'class': 'abstract', 'rows': 4}
            ),
            'css_class': forms.Select(
                choices=conf.VIDEO_CSS_CLASSES,
            ),
            'description': forms.Textarea(
                attrs={'class': 'description', 'rows': 8}
            ),
            'height': forms.Select(
                attrs={'class': 'size'},
                choices=conf.VIDEO_HEIGHTS,
            ),
            'name': forms.Textarea(
                attrs={'class': 'abstract', 'rows': 2}
            ),
            'width': forms.Select(
                attrs={'class': 'size'},
                choices=conf.VIDEO_WIDTHS,
            ),
        }


class VideoPlugin(CMSPluginBase):
    allow_children = conf.VIDEO_ALLOW_CHILDREN
    child_classes = conf.VIDEO_PLUGINS
    fieldsets = conf.VIDEO_FIELDSETS
    form = VideoPluginForm
    model = Video
    module = _('content')
    name = _('video')
    render_template = 'cms/plugins/videos_video.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'indicator_hidden': get_indicator_hidden(request, instance),
        })
        return context


plugin_pool.register_plugin(VideoPlugin)
