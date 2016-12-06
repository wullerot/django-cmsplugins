from __future__ import unicode_literals

from django import forms
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse_lazy


class AnchorWidget(forms.TextInput):
    class Media:
        css = {
            'screen': [static('links/cms.page.anchor.css')],
        }
        js = [
            static('links/cms.page.anchor.js'),
        ]

    def render(self, name, value, attrs=None):
        kwargs = {
            'class': 'cms_page_anchor',
            'data-url': '/admin/links/baselink/anchors/'
        }
        final_attrs = self.build_attrs(attrs, **kwargs)
        return super(AnchorWidget, self).render(name, value, attrs=final_attrs)
