# Generated by Django 2.2.12 on 2020-05-08 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('columns', '0004_auto_20181205_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='cms_page',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='columns_column_set', to='cms.Page'),
        ),
    ]
