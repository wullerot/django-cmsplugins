from __future__ import unicode_literals

from django.contrib import admin

from .conf import CMSPluginSiteConf, CMSPluginSiteConfAdmin


admin.site.register(CMSPluginSiteConf, CMSPluginSiteConfAdmin)
