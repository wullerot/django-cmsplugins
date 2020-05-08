from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PageField
from filer.fields.file import FilerFileField


@python_2_unicode_compatible
class BaseLink(models.Model):

    plugin = models.OneToOneField(
        'cms.CMSPlugin',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
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
