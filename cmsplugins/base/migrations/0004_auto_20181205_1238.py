# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('base', '0003_auto_20181205_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSPluginSiteConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField(blank=True, default='{}', verbose_name='Settings')),
                ('site', models.OneToOneField(default=1, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.Site')),
            ],
            options={
                'ordering': ['site', 'id'],
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.RemoveField(
            model_name='cmspluginconf',
            name='site',
        ),
        migrations.DeleteModel(
            name='CMSPluginConf',
        ),
    ]
