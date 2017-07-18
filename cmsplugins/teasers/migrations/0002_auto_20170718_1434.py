# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 12:34
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
        ('teasers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaser',
            name='filer_image',
            field=filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teasers_teaser_filer_image_set', to='filer.Image', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='teaser',
            name='link_cms',
            field=cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Page'),
        ),
        migrations.AlterField(
            model_name='teaser',
            name='filer_icon',
            field=filer.fields.file.FilerFileField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teasers_teaser_filer_icon_set', to='filer.File', verbose_name='Icon'),
        ),
    ]
