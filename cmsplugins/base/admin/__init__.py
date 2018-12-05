from __future__ import unicode_literals

from django.contrib import admin

from .conf import CMSPluginConf, CMSPluginConfAdmin


admin.site.register(CMSPluginConf, CMSPluginConfAdmin)
