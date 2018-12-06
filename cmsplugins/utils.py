from __future__ import unicode_literals

from importlib import import_module

from django import forms
from django.conf import settings
from django.utils import six
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _


def get_indicator_hidden(request, instance):
    html = ''
    is_visible = getattr(instance, 'is_visible', True)
    if request.toolbar.edit_mode and not is_visible:
        name = _('hidden')
        css_class = 'plugin-indicator-hidden'
        html = '<span class="{}">{}</span>'.format(
            css_class,
            name,
        )
    return mark_safe(html)


def get_str_from_tuple(key='', properties=()):
    return dict((k, v) for k, v in properties).get(key, '')


def load_object(import_path):
    if not isinstance(import_path, six.string_types):
        return import_path
    if '.' not in import_path:
        raise TypeError(
            "'import_path' argument to 'django_load.core.load_object'"
            " must contain at least one dot."
        )
    module_name, object_name = import_path.rsplit('.', 1)
    module = import_module(module_name)
    return getattr(module, object_name)


def get_widget_class(widget_name):
    if not widget_name:
        return None
    # TODO clean up this mess
    if isinstance(widget_name, six.string_types):
        modules = widget_name.split('.')
        if len(modules) == 1:
            module = forms
        else:
            try:
                module = import_module('.'.join(modules[:-1]))
            except Exception:
                pass
        if module:
            return getattr(module, modules[-1], None)
        return None
    try:
        if issubclass(widget_name, forms.Widget):
            return widget_name
    except Exception:
        pass
    return None


def get_plugin_conf(plugin_type):
    """
    load the plugin conf from settings
    TODO load them from cache/db
    """
    if hasattr(settings, 'CMSPLUGINS'):
        return settings.CMSPLUGINS.get(plugin_type, {})
    return {}
