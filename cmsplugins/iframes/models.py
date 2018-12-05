from __future__ import unicode_literals

from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from cmsplugins.base.models import BasePlugin
from filer.fields.image import FilerImageField

from . import conf


# TODO check that the markup is an iframe and there is no script in it
class IFrame(BasePlugin):
    markup = models.TextField(
        max_length=700,
        verbose_name=_('iframe code'),
    )

    @property
    def iframe(self):
        if self.markup:
            return mark_safe(self.markup)
        else:
            return ''
