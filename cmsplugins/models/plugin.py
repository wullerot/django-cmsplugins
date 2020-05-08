from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page


@python_2_unicode_compatible
class BasePlugin(CMSPlugin):

    cmsplugin = True

    bg_color = models.CharField(
        max_length=200,
        blank=True,
        default='',
        verbose_name=_('bg color'),
    )
    css_class = models.CharField(
        max_length=200,
        blank=True,
        default='',
        verbose_name=_('css class'),
    )
    in_navigation = models.BooleanField(
        default=False,
        verbose_name=_('in navigation'),
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name=_('visible'),
    )
    height = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('height'),
    )
    width = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name=_('width'),
    )
    name = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name=_('title'),
    )
    show_name = models.BooleanField(
        default=True,
        verbose_name=_('display title'),
    )
    slug = models.SlugField(
        max_length=150,
        default='',
        blank=True,
        editable=False,
        verbose_name=_('slug'),
    )
    cms_page = models.ForeignKey(
        Page,
        editable=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_set',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return '{} {} {}'.format(
            self.position,
            self._meta.verbose_name,
            self.pk,
        )

    def save(self, *args, **kwargs):
        if self.placeholder.page:
            self.cms_page_id = self.placeholder.page.id
        if self.name:
            self.slug = '{}-{}'.format(
                slugify(self.name),
                self.position
            )
        else:
            self.slug = 'section-{0}'.format(self.position)
        super(BasePlugin, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.cms_page:
            return '{}#{}'.format(
                self.cms_page.get_absolute_url(),
                self.slug
            )
        return ''
    get_absolute_url.short_description = _('Absolute URL')

    @property
    def css_classes(self):
        classes = []
        if self.height:
            classes.append(self.height)
        if self.width:
            classes.append(self.width)
        if self.css_class:
            classes.append(self.css_class)
        if classes:
            return ' {}'.format(' '.join(classes))
        else:
            return ''

    @property
    def menu_title(self):
        if self.name:
            return '{}'.format(self.name)
        else:
            return '{}'.format(self.slug)

    @property
    def title(self):
        if self.show_name and self.name:
            return '{}'.format(self.name)
