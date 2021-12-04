# Generated by Django 3.2.9 on 2021-11-29 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sharetech', '0007_alter_categorymst_parent_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_status', models.PositiveSmallIntegerField(default=1, verbose_name='申込ステータス')),
                ('apply_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='申込日')),
                ('id_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update Date')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete Date')),
                ('consult_window_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sharetech.consultwindow', verbose_name='相談窓口ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='申込者ID')),
            ],
            options={
                'db_table': 'consult_apply',
            },
        ),
        migrations.AddConstraint(
            model_name='consultapply',
            constraint=models.UniqueConstraint(fields=('consult_window_id', 'user_id', 'apply_date'), name='apply_unique'),
        ),
    ]
