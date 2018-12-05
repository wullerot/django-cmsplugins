from __future__ import unicode_literals

# from importlib import import_module

from django import forms
from django.conf import settings


class CMSPluginForm(forms.ModelForm):

    _conf = {}
    _plugin_type = None

    def __init__(self, *args, **kwargs):
        super(CMSPluginForm, self).__init__(*args, **kwargs)
        self._plugin_type = self.get_plugin_type(**kwargs)
        self._conf = self.get_plugin_conf()
        self.set_widgets()

    def get_plugin_type(self, **kwargs):
        instance = kwargs.get('instance', None)
        if instance:
            return instance.plugin_type
        initial = kwargs.get('initial')
        if initial:
            return initial.get('plugin_type', '')
        return ''

    def get_plugin_conf(self):
        return settings.CMSPLUGINS.get(self._plugin_type, None)

    def set_widgets(self):
        widgets = self._conf.get('widgets', {})
        for k, f in widgets.items():
            # TODO defunc atm, we need to be able to load custom widgets here
            print getattr(forms, f['widget'], None)
            if k in self._meta.fields:
                field_class = getattr(forms, f['widget'], None)
                kwargs = {}
                if f.get('choices'):
                    if not field_class:
                        field_class = forms.Select
                    kwargs['choices'] = f.get('choices')
                if f.get('attrs'):
                    kwargs['attrs'] = f.get('attrs')
                if f.get('conf'):
                    kwargs['conf'] = f.get('conf')
                self.fields[k].widget = field_class(**kwargs)
