# Generated by Django 3.2.9 on 2021-12-09 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharetech', '0009_customuser_tmp_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='industrymst',
            old_name='industry_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='occupationmst',
            old_name='occupation_name',
            new_name='oname',
        ),
        migrations.RenameField(
            model_name='positionmst',
            old_name='position_name',
            new_name='name',
        ),
    ]