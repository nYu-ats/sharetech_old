# Generated by Django 3.2.9 on 2021-11-21 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sharetech', '0003_categoryconsultwindowmapping_categorymst_consultwindow'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultwindow',
            name='archivement',
            field=models.CharField(default='', max_length=512, verbose_name='実績'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='categoryconsultwindowmapping',
            constraint=models.UniqueConstraint(fields=('category_id', 'consult_window_id'), name='mapping_unique'),
        ),
    ]
