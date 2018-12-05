from __future__ import unicode_literals

import json

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CMSPluginSiteConfManager(models.Manager):

    def get_active(self, request):
        qs = self.get_queryset().filter(site=request.site)
        return qs.first()


class CMSPluginSiteConf(models.Model):

    objects = CMSPluginSiteConfManager()

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

    def __init__(self, *args, **kwargs):
        super(CMSPluginSiteConf, self).__init__(*args, **kwargs)
        try:
            self.settings = json.loads(self.json)
        except Exception as e:
            print e
            self.settings = {}
        print self.settings

    def __str__(self):
        if self.site:
            return '{}'.format(self.site.name)
        return '{} {}'.format(_('Settings'), self.pk)

    def get_plugin_conf(self, plugin_name):
        return []


class CMSPluginConfManager(models.Manager):

    pass


class CMSPluginConf(models.Model):

    objects = CMSPluginConfManager()

    site_conf = models.ForeignKey(
        CMSPluginSiteConf,
        on_delete=models.CASCADE,
    )
    plugin_name = models.CharField(
        max_length=100,
        default='',
        verbose_name=_('Plugin'),
    )
    fieldsets = models.TextField(
        blank=True,
        default='{}',
        verbose_name=_('Fieldsets')
    )
    required_fields = models.TextField(
        blank=True,
        default='{}',
        verbose_name=_('Fieldsets')
    )

    class Meta:
        ordering = ['site_conf', 'plugin_name']
        verbose_name = _('Plugin')
        verbose_name_plural = _('Plugins')

    def __str__(self):
        return '{}'.format(self.plugin_name)
