from __future__ import unicode_literals

from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from baseplugin.models import BasePlugin
from filer.fields.image import FilerImageField

from . import conf


class Gallery(BasePlugin):
    # TODO add more layouts
    layout = models.CharField(_('type'), max_length=20, blank=True, default='')
    abstract = models.TextField(_('short description'), max_length=150,
                                blank=True, default='')
    description = models.TextField(_('long description '), blank=True,
                                   default='')

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
    show_popup = models.BooleanField(_('show popup'), default=False)
    image = FilerImageField(verbose_name=_('image'), null=True, default=None,
                            on_delete=models.SET_NULL)
    abstract = models.TextField(_('short description'), blank=True, default='')
    description = models.TextField(_('long description '), blank=True,
                                   default='')
