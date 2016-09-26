from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


@python_2_unicode_compatible
class BasePlugin(CMSPlugin):
    css_class = models.CharField(_('css class'), max_length=200, blank=True,
                                 default='')
    in_navigation = models.BooleanField(_('in navigation'), default=False)
    is_visible = models.BooleanField(_('visible'), default=True)
    height = models.CharField(_('height'), max_length=100, blank=True,
                              default='')
    width = models.CharField(_('width'), max_length=50, blank=True, default='')
    name = models.CharField(_('title'), max_length=150, default='', blank=True)
    show_name = models.BooleanField(_('display title'), default=True)
    slug = models.SlugField(_('slug'), max_length=150, default='', blank=True,
                            editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        if self.is_visible:
            hidden = ''
        else:
            hidden = ' | {0}'.format(_('(hidden)'))
        return '{0}{1}'.format(' '.join(self.name.splitlines()), hidden)

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = '{0}'.format(slugify(self.name))
        else:
            self.slug = 'section-{0}'.format(self.pk)
        super(BasePlugin, self).save(*args, **kwargs)

    @property
    def css_classes(self):
        classes = []
        if self.height:
            classes.append(self.height)
        if self.width:
            classes.append(self.width)
        if self.css_class:
            classes.append(self.css_classes)
        if classes:
            return ' {0}'.format(' '.join(classes))
        else:
            return ''

    @property
    def menu_title(self):
        if self.name:
            return '{0}'.format(self.name)
        else:
            return '{0}'.format(self.slug)

    @property
    def title(self):
        if self.show_name and self.name:
            return '{0}'.format(self.name)
