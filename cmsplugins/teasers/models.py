from __future__ import unicode_literals

from django.apps import apps
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
from cms.models.fields import PageField
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

from . import conf


@python_2_unicode_compatible
class TeaserWrap(CMSPlugin):
    css_class = models.CharField(
        max_length=200,
        blank=True,
        default='',
        verbose_name=_('CSS class'),
    )
    in_navigation = models.BooleanField(
        default=False,
        verbose_name=_('In navigation'),
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name=_('Visible'),
    )
    height = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('Height'),
    )
    width = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name=_('Width'),
    )
    name = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name=_('Name'),
    )
    slug = models.SlugField(
        max_length=150,
        default='',
        blank=True,
        editable=False,
        verbose_name=_('Slug'),
    )
    cms_page = models.ForeignKey(
        Page,
        editable=False,
        null=True,
        related_name="cms_teasers_wrap_set"
    )

    class Meta:
        verbose_name = _('Teasers Wrap')
        verbose_name_plural = _('Teasers Wraps')

    def __str__(self):
        return '{}'.format(self.name or self.pk or '')

    def save(self, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(TeaserWrap, self).save(**kwargs)


class Teaser(CMSPlugin):
    link_cms = PageField(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Page'),
    )
    name = models.CharField(
        max_length=150,
        blank=True,
        default='',
        verbose_name=_('Name'),
    )
    body = models.TextField(
        default='',
        blank=True,
        verbose_name=_('Text'),
    )
    filer_icon = FilerFileField(
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('Icon'),
        related_name='teasers_teaser_filer_icon_set',
    )
    filer_image = FilerImageField(
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('Image'),
        related_name='teasers_teaser_filer_image_set',
    )

    class Meta:
        verbose_name = _('Teaser')
        verbose_name_plural = _('Teasers')

    def __str__(self):
        return '{}'.format(self.name or self.pk or '')

    def save(self, **kwargs):
        super(Teaser, self).save(**kwargs)

    def get_image(self):
        if self.filer_image:
            return self.filer_image
        elif self.link_cms:
            img_obj = self.get_page_info()
            if img_obj:
                return img_obj.image

    def get_name(self):
        if self.name:
            return self.name
        elif self.link_cms:
            name_obj = self.get_page_info()
            if name_obj:
                return name_obj.name

    def get_body(self):
        if self.body:
            return self.body
        elif self.link_cms:
            body_obj = self.get_page_info()
            if body_obj:
                return body_obj.abstract or body_obj.description

    def copy_relations(self, original):
        link = original.get_link()
        if link:
            link.id = None
            link.teaser = self
            link.save()

    def get_link(self):
        link = None
        if conf.TEASER_LINK_MODEL:
            field_name = self.get_link_field_name()
            if field_name:
                link = getattr(self, field_name, None)
        return link

    def get_link_field_name(self):
        field_name = None
        if conf.TEASER_LINK_MODEL:
            for f in self._meta.get_fields():
                if f.one_to_one:
                    field_model = '{}.{}'.format(
                        f.related_model._meta.app_label,
                        f.related_model._meta.model_name,
                    )
                    if field_model == conf.TEASER_LINK_MODEL.lower():
                        field_name = f.name
                        break
        return field_name

    def get_page_info(self):
        if conf.TEASER_PAGE_INFO_MODELS:
            info_obj = None
            for m in conf.TEASER_PAGE_INFO_MODELS:
                model = apps.get_model(m)
                obj = model.objects.filter(cms_page=self.link_cms).first()
                if obj:
                    info_obj = obj
                    break
            return info_obj
        return None

    @property
    def link(self):
        if conf.TEASER_LINK_MODEL:
            return self.get_link()


class TeaserLinkMixin(models.Model):

    teaser = models.OneToOneField(
        Teaser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Teaser')
    )

    class Meta:
        abstract = True
