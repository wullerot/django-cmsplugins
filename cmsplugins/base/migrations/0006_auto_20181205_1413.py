# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20181205_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmspluginconf',
            name='conf_str',
        ),
        migrations.AddField(
            model_name='cmspluginconf',
            name='fieldsets',
            field=models.TextField(blank=True, default='{}', verbose_name='Fieldsets'),
        ),
        migrations.AddField(
            model_name='cmspluginconf',
            name='required_fields',
            field=models.TextField(blank=True, default='{}', verbose_name='Fieldsets'),
        ),
    ]
