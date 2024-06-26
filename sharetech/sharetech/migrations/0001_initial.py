# Generated by Django 3.2.9 on 2021-11-11 13:51

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sharetech.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_name', models.CharField(max_length=64, verbose_name='Industry Name')),
                ('id_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update Date')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete Date')),
            ],
            options={
                'db_table': 'industry_mst',
            },
        ),
        migrations.CreateModel(
            name='OccupationMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_name', models.CharField(max_length=64, verbose_name='Occupation Name')),
                ('id_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update Date')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete Date')),
            ],
            options={
                'db_table': 'occupation_mst',
            },
        ),
        migrations.CreateModel(
            name='PositionMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=64, verbose_name='Position Name')),
                ('id_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update Date')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete Date')),
            ],
            options={
                'db_table': 'position_mst',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name_jp', models.CharField(help_text='必須項目です。全角文字で20文字以下にしてください。', max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='First Name Japanese')),
                ('family_name_jp', models.CharField(help_text='必須項目です。全角文字で20文字以下にしてください。', max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Family Name Japanese')),
                ('first_name_en', models.CharField(help_text='必須項目です。全角文字で20文字以下にしてください。', max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='First Name Englist')),
                ('family_name_en', models.CharField(help_text='必須項目です。全角文字で20文字以下にしてください。', max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Family Name Englist')),
                ('username_kana', models.CharField(help_text='必須項目です。全角文字で50文字以下にしてください。', max_length=64, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Name Kana')),
                ('role_code', models.CharField(choices=[('1', '専門家'), ('2', '一般')], max_length=1, verbose_name='Account Role')),
                ('icon_path', models.CharField(max_length=512, null=True, verbose_name='Icon Image Path')),
                ('introduction', models.CharField(max_length=512, null=True, verbose_name='Introduction')),
                ('company', models.CharField(max_length=256, verbose_name='Company')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(30)], verbose_name='password')),
                ('email_verified_at', models.DateTimeField(null=True, verbose_name='メールアドレス確認日')),
                ('remember_token', models.CharField(max_length=512, null=True, verbose_name='トークン')),
                ('id_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('login_counter', models.PositiveIntegerField(default=0, verbose_name='Login Counter')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Update Date')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete Date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('industry_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sharetech.industrymst', verbose_name='Industry ID')),
                ('occupation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sharetech.occupationmst', verbose_name='Occupation ID')),
                ('position_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sharetech.positionmst', verbose_name='Position ID')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', sharetech.models.user.CustomUserManager()),
            ],
        ),
    ]
