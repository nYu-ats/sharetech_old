# Generated by Django 3.2.9 on 2021-11-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharetech', '0005_alter_categoryconsultwindowmapping_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymst',
            name='category_hierarchy',
            field=models.SmallIntegerField(default=1, verbose_name='カテゴリ階層'),
        ),
    ]
