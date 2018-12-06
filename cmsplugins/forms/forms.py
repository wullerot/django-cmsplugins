from __future__ import unicode_literals

from django import forms

from cmsplugins.utils import get_widget_class, get_plugin_conf


class CMSPluginForm(forms.ModelForm):

    _conf = {}
    _plugin_type = None

    def __init__(self, *args, **kwargs):
        super(CMSPluginForm, self).__init__(*args, **kwargs)
        self._conf = get_plugin_conf(self.get_plugin_type(**kwargs))
        self.set_fields()

    def get_plugin_type(self, **kwargs):
        instance = kwargs.get('instance', None)
        if instance:
            return instance.plugin_type
        initial = kwargs.get('initial')
        if initial:
            return initial.get('plugin_type', '')
        return ''

    def set_fields(self):
        """
        set the fields widget
        set if field is required
        """
        widgets = self._conf.get('widgets', {})
        required_fields = self._conf.get('required_fields', [])
        for k, f in widgets.items():
            if k in self._meta.fields:
                widget_class = get_widget_class(f.get('widget'))
                kwargs = {}
                if f.get('choices'):
                    if not widget_class:
                        widget_class = forms.Select
                    kwargs['choices'] = f.get('choices')
                elif getattr(self.fields[k].widget, 'choices', None):
                    kwargs['choices'] = self.fields[k].widget.choices
                elif not widget_class:
                    widget_class = self.fields[k].widget.__class__
                if f.get('attrs'):
                    kwargs['attrs'] = f.get('attrs')
                if f.get('conf'):
                    kwargs['conf'] = f.get('conf')
                self.fields[k].widget = widget_class(**kwargs)
                if k in required_fields:
                    self.fields[k].required = True
