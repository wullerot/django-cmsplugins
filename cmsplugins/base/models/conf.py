from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CMSPluginConf(models.Model):

    site = models.OneToOneField(
        'sites.Site',
        null=True,
        default=settings.SITE_ID,
        on_delete=models.SET_NULL,
        editable=False,
    )

    class Meta:
        ordering = ['site', 'id']
        verbose_name = _('Settings')
        verbose_name_plural = _('Settings')

    def __str__(self):
        if self.site:
            return '{}'.format(self.site.name)
        return '{} {}'.format(_('Settings'), self.pk)
