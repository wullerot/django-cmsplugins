from __future__ import unicode_literals

# from cmsplugins.base.models import CMSPluginSiteConf


class CMSPluginMixin(object):

    def __init__(self, *args, **kwargs):
        super(CMSPluginMixin, self).__init__(*args, **kwargs)

    def get_fieldsets(self, request, obj=None):
        """
        conf = CMSPluginSiteConf.objects.get_active(request=request)
        plugin_conf = conf.get_plugin_conf()
        if fieldsets:
            return fieldsets
        """
        fieldsets = super(CMSPluginMixin, self).get_fieldsets(request, obj=obj)
        return fieldsets
