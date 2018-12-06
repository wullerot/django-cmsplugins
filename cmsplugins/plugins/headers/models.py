from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cmsplugins.models import BasePlugin
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Header(BasePlugin):

    abstract = models.TextField(
        max_length=250,
        default='',
        blank=True,
        verbose_name=_('abstract'),
    )
    description = models.TextField(
        max_length=250,
        default='',
        blank=True,
        verbose_name=_('descrition'),
    )
    text_position = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('text position'),
    )
    text_color = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('text color'),
    )
    image = FilerImageField(
        null=True,
        default=None,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('image'),
    )

    def __str__(self):
        if self.is_visible:
            hidden = ''
        else:
            hidden = ' {0}'.format(_('(hidden)'))
        if self.name:
            return '{0}{1}'.format(' '.join(self.name.splitlines()), hidden)
        elif self.image:
            return '{0}{1}'.format(self.image.name or self.image, hidden)
        else:
            return '{0}'.format(hidden)

    @property
    def css_classes(self):
        classes = []
        if self.height:
            classes.append(self.height)
        if self.width:
            classes.append(self.width)
        if self.text_color:
            classes.append(self.text_color)
        if self.text_position:
            classes.append(self.text_position)
        if self.css_class:
            classes.append(self.css_class)
        if classes:
            return ' {0}'.format(' '.join(classes))
        else:
            return ''
