from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CMSPluginBaseConfig(AppConfig):
    name = 'cmsplugins.base'
    verbose_name = _('Django CMS Plugins')
