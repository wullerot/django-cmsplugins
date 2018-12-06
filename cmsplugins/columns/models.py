from __future__ import unicode_literals

from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

from cmsplugins.base.models import BasePlugin
from filer.fields.image import FilerImageField


class Column(BasePlugin):

    bg_image = FilerImageField(
        null=True,
        default=None,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='columns_column_bg_image_set',
        verbose_name=_('background image'),
    )

    @property
    def css_classes(self):
        classes = []
        if self.width:
            classes.append(self.width)
        if self.height:
            classes.append(self.height)
        if self.bg_color:
            classes.append(self.bg_color)
        if self.css_class:
            classes.append(self.css_class)
        if classes:
            return ' {0}'.format(' '.join(classes))
        else:
            return ''

    @property
    def html_style(self):
        html = ''
        if self.bg_image:
            html = ' style="background-image: url({0});"'.format(
                self.bg_image.url,
            )
        return mark_safe(html)
