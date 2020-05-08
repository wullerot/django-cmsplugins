# Generated by Django 2.2.12 on 2020-05-08 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_googlemap_bg_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlemap',
            name='cms_page',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maps_googlemap_set', to='cms.Page'),
        ),
    ]