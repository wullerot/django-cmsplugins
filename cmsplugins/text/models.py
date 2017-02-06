from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from cmsplugins.baseplugin.models import BasePlugin


@python_2_unicode_compatible
class Text(BasePlugin):
    """
    Plain Text Plugin
    """

    body = models.TextField(_('body'), default='')

    def __str__(self):
        string = strip_tags(' '.join(self.body.splitlines()))
        return '{0}'.format(string[:60])
