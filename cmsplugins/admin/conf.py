from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from ..models import CMSPluginConf, CMSPluginSiteConf


class CMSPluginConfInlineForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = CMSPluginConf
        widgets = {}


class CMSPluginConfInline(admin.StackedInline):

    extra = 0
    form = CMSPluginConfInlineForm
    model = CMSPluginConf


class CMSPluginSiteConfAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = CMSPluginSiteConf
        widgets = {}


class CMSPluginSiteConfAdmin(admin.ModelAdmin):

    form = CMSPluginSiteConfAdminForm
    inlines = [CMSPluginConfInline]
