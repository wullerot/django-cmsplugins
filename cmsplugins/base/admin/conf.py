from __future__ import unicode_literals

from django import forms
# from django.conf import settings
from django.contrib import admin

from cms.plugin_pool import plugin_pool

from ..models import CMSPluginConf


class CMSPluginConfAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = CMSPluginConf
        widgets = {}

    def __init__(self, *args, **kwargs):
        plugin_list = self.get_plugin_list() # NOQA
        super(CMSPluginConfAdminForm, self).__init__(*args, **kwargs)

    def get_plugin_list(self):
        for p in plugin_pool.get_all_plugins():
            for k, v in p.__dict__.items():
                print k, v
        return []


class CMSPluginConfAdmin(admin.ModelAdmin):

    form = CMSPluginConfAdminForm
