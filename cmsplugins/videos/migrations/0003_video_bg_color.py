# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_cms_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='bg_color',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='bg color'),
        ),
    ]
