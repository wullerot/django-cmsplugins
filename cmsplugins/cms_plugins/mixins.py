from __future__ import unicode_literals

# from cmsplugins.models import CMSPluginSiteConf

from cmsplugins.utils import get_plugin_conf


class CMSPluginMixin(object):

    def __init__(self, *args, **kwargs):
        super(CMSPluginMixin, self).__init__(*args, **kwargs)
        self._conf = get_plugin_conf(plugin_type=self.get_plugin_type())

    def get_fieldsets(self, request, obj=None):
        fieldsets = self._conf.get('fieldsets')
        if not fieldsets:
            fieldsets = super(CMSPluginMixin, self).get_fieldsets(
                request,
                obj=obj
            )
        return fieldsets

    def get_plugin_type(self, **kwargs):
        return self.__class__.__name__
