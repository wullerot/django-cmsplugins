from __future__ import unicode_literals

from django.apps import apps
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from baseplugin.models import BasePlugin, BaseLink
from baseplugin.utils import load_object
from filer.fields.image import FilerImageField

from . import conf


class Slider(BasePlugin):
    autoplay = models.BooleanField(_('auto play'), default=True)
    loop = models.BooleanField(_('loop'), default=False)
    arrows = models.BooleanField(_('show arrows'), default=False)
    indicators = models.BooleanField(_('show indicators'), default=False)

    @property
    def html_data(self):
        html = ''
        if self.loop:
            html += ' data-loop="true"'
        if self.autoplay:
            html += ' data-autoplay="true"'
        if self.arrows:
            html += ' data-arrows="true"'
        if self.indicators:
            html += ' data-indicators="true"'
        return mark_safe(html)

    def copy_relations(self, draft):
        if hasattr(self, 'plugin_link'):
            self.plugin_link.delete()
        if hasattr(draft, 'plugin_link'):
            link = draft.plugin_link
            link.pk = None
            link.plugin_id = self.id
            link.save()

    @property
    def link(self):
        return getattr(self, 'plugin_link', None)


@python_2_unicode_compatible
class Slide(BasePlugin):
    # TODO implement animation framework
    abstract = models.TextField(_('abstract'), default='', blank=True)
    description = models.TextField(_('description'), default='', blank=True)
    text_animation = models.CharField(_('text animation'), max_length=50,
                                      blank=True, default='')
    text_color = models.CharField(_('text color'), max_length=100,
                                  blank=True, default='')
    text_position = models.CharField(_('text position'), max_length=100,
                                     blank=True, default='')
    image = FilerImageField(verbose_name=_('image'), null=True, default=None,
                            on_delete=models.SET_NULL, related_name='+')
    image_animation = models.CharField(_('image animation'), max_length=50,
                                       blank=True, default='')

    def __str__(self):
        if self.is_visible:
            hidden = ''
        else:
            hidden = ' {0}'.format(_('(hidden)'))
        if self.name:
            return '{0}{1}'.format(' '.join(self.name.splitlines()), hidden)
        elif self.image:
            return '{0}{1}'.format(self.image.name or self.image, hidden)
        else:
            return '{0}'.format(hidden)

    def copy_relations(self, draft):
        if hasattr(self, 'plugin_link'):
            self.plugin_link.delete()
        if hasattr(draft, 'plugin_link'):
            link = draft.plugin_link
            link.pk = None
            link.plugin_id = self.id
            link.save()

    @property
    def css_classes(self):
        classes = []
        if self.text_color:
            classes.append(self.text_color)
        if self.text_position:
            classes.append(self.text_position)
        if self.css_class:
            classes.append(self.css_class)
        if classes:
            return ' {0}'.format(' '.join(classes))
        else:
            return ''

    @property
    def html_data(self):
        html = ''
        if self.text_animation:
            html += ' data-text-animation="{0}"'.format(self.text_animation)
        if self.image_animation:
            html += ' data-image-animation="{0}"'.format(self.image_animation)
        return mark_safe(html)

    @property
    def link(self):
        return getattr(self, 'plugin_link', None)


class Link(BaseLink):
    class Meta:
        abstract = False
