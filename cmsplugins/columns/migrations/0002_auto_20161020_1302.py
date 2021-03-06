# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-20 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('columns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='bg_color',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='background color'),
        ),
        migrations.AddField(
            model_name='column',
            name='bg_image',
            field=filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='columns_column_bg_image_set', to='filer.Image', verbose_name='background image'),
        ),
    ]
