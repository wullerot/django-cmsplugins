from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.models import BasePlugin
from filer.fields.image import FilerImageField


class Gallery(BasePlugin):
    # TODO add more layouts
    layout = models.CharField(
        max_length=20,
        blank=True,
        default='',
        verbose_name=_('type'),
    )
    abstract = models.TextField(
        max_length=150,
        blank=True,
        default='',
        verbose_name=_('short description'),
    )
    description = models.TextField(
        blank=True,
        default='',
        verbose_name=_('long description '),
    )

    @property
    def css_classes(self):
        classes = [self.gallery_layout]
        if self.height:
            classes.append(self.height)
        if self.width:
            classes.append(self.width)
        if self.css_class:
            classes.append(self.css_class)
        if classes:
            return ' {0}'.format(' '.join(classes))
        else:
            return ''

    @property
    def gallery_layout(self):
        if not self.layout:
            return 'standard'


class Picture(BasePlugin):
    show_popup = models.BooleanField(
        default=False,
        verbose_name=_('show popup'),
    )
    image = FilerImageField(
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('image'),
    )
    abstract = models.TextField(
        blank=True,
        default='',
        verbose_name=_('short description'),
    )
    description = models.TextField(
        blank=True,
        default='',
        verbose_name=_('long description '),
    )
