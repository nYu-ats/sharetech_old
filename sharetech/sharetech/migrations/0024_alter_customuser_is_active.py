# Generated by Django 4.0 on 2022-01-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharetech', '0023_customuser_is_active_alter_customuser_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Activated'),
        ),
    ]
