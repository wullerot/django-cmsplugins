from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from baseplugin.models import BasePlugin
from filer.fields.image import FilerImageField

from . import conf


@python_2_unicode_compatible
class Header(BasePlugin):
    abstract = models.TextField(_('abstract'), max_length=250, default='',
                                blank=True)
    description = models.TextField(_('descrition'), max_length=250, default='',
                                   blank=True)
    text_position = models.CharField(_('text position'), max_length=100,
                                     blank=True, default='')
    text_color = models.CharField(_('text color'), max_length=100, blank=True,
                                  default='')
    image = FilerImageField(verbose_name=_('image'), null=True, default=None,
                            blank=True, on_delete=models.SET_NULL,
                            related_name='+')

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
