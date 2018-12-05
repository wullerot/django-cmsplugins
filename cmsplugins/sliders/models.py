from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cmsplugins.base.models import BasePlugin, BaseLink
from filer.fields.image import FilerImageField


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

    name_sub = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name=_('Subtitle'),
    )
    abstract = models.TextField(
        default='',
        blank=True,
        verbose_name=_('abstract'),
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name=_('description'),
    )
    text_animation = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name=_('text animation'),
    )
    text_color = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('text color'),
    )
    text_position = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('text position'),
    )
    image = FilerImageField(
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('image'),
    )
    image_animation = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name=_('image animation'),
    )

    def __str__(self):
        if self.is_visible:
            hidden = ''
        else:
            hidden = ' {0}'.format(_('(hidden)'))
        if self.full_name:
            return '{0}{1}'.format(self.full_name, hidden)
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
        if hasattr(self, 'slide_link'):
            self.slide_link.delete()
        if hasattr(draft, 'slide_link'):
            link = draft.slide_link
            link.pk = None
            link.plugin_id = self.id
            link.save()

    def get_image(self):
        return self.image

    def get_title(self):
        return self.name

    def get_subtitle(self):
        return self.name_sub

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
    def full_name(self):
        names = []
        if self.name:
            names.append(' '.join(self.name.splitlines()))
        if self.name_sub:
            names.append(' '.join(self.name_sub.splitlines()))
        name = ' '.join(names)
        return name.strip()

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
