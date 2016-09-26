from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from baseplugin.models import BasePlugin
from baseplugin.utils import get_str_from_tuple
from filer.fields.image import FilerImageField

from . import conf


@python_2_unicode_compatible
class Column(BasePlugin):

    def __str__(self):
        name = ''
        names = []
        if self.name:
            names.append(self.name)
        if self.width:
            width = get_str_from_tuple(self.width, conf.COLUMN_WIDTHS)
            names.append('| {0}'.format(width))
        if not self.is_visible:
            names.append('| {0}'.format(_('(hidden)')))
        if names:
            name = ' '.join(names)
        return name
