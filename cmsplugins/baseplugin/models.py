from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
from cms.models.fields import PageField
from filer.fields.file import FilerFileField


@python_2_unicode_compatible
class BasePlugin(CMSPlugin):
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
    )

    class Meta:
        abstract = True

    def __str__(self):
        if self.is_visible:
            hidden = ''
        else:
            hidden = ' | {0}'.format(_('(hidden)'))
        return '{0}{1}'.format(' '.join(self.name.splitlines()), hidden)

    def save(self, *args, **kwargs):
        if self.page:
            self.cms_page_id = self.page.id
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
            classes.append(self.css_class)
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


@python_2_unicode_compatible
class BaseLink(models.Model):
    plugin = models.OneToOneField(
        CMSPlugin,
        null=True,
        blank=True,
        related_name='plugin_link'
    )
    name = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name=_('title'),
    )
    abstract = models.TextField(
        max_length=250,
        default='',
        blank=True,
        verbose_name=_('abstract'),
    )
    cms_page = PageField(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('page'),
    )
    anchor = models.CharField(
        max_length=150,
        blank=True,
        default='',
        verbose_name=_('anchor'),
    )
    filer_file = FilerFileField(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('file'),
    )
    url = models.URLField(
        max_length=255,
        blank=True,
        default='',
        verbose_name=_('URL'),
    )
    email = models.EmailField(
        blank=True,
        default='',
        verbose_name=_('Email'),
    )

    class Meta:
        abstract = True
        verbose_name = _('link')
        verbose_name_plural = _('links')

    def __str__(self):
        return 'link'

    def get_email(self):
        return self.email

    def get_link(self):
        if self.cms_page:
            return self.cms_page.get_absolute_url()
        elif self.filer_file:
            return self.filer_file.url
        elif self.url:
            return self.url
        elif self.email:
            return 'mailto:{0}'.format(self.email)
        else:
            return ''

    def get_target(self):
        if not self.cms_page and (self.filer_file or self.url):
            return '_blank'
        else:
            return ''

    @property
    def href(self):
        return self.get_link()

    @property
    def target_tag(self):
        target = self.get_target()
        if target:
            return mark_safe(' target="{0}"'.format(target))
        else:
            return ''
