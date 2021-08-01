from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator,MaxValueValidator, MinValueValidator
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django import forms

# ユーザーマネージャカスタム
class UseManager(BaseUserManager):
    """
    メールアドレスでユーザー作成
    """
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        下記必須項目でユーザー作成
        ・ユーザー名
        ・メールアドレス
        ・パスワード
        """
        if not username:
            raise ValueError('ユーザー名は必須の項目です。')

        if not email:
            raise ValueError('メールアドレスは必須の項目です。')

        new_email = self.normalize_email(email)
        new_name = self.model.normalize_usrname(username)
        new_user = self.model(username= new_name, email=new_email, **extra_fields)
        new_user.set_password(password)
        new_user.save(using=self._db)
        
        return new_user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        デフォルト項目あればこっちで設定
        ・権限
        """
        extra_fields.setdefault('role_id', **extra_fields.get('role_id'))
        return self._create_user(username, email, password, **extra_fields)


# ユーザーモデルカスタマイズ
class User(AbstractBaseUser, PermissionsMixin):
    """
    Django標準Userモデル拡張
    
    """

    class Meta:
        db_table = 'user'
    
    username_validator = UnicodeUsernameValidator()

    """
    columns
    """
    # ユーザー名
    username = models.CharField(
        verbose_name = 'Name',
        help_text='必須項目です。全角文字、半角英数字、@/./+/-/_で50文字以下にしてください。',
        max_length = 50,
        validators=[username_validator],
        blank=False
    )

    # 権限
    role_id = models.IntegerField(
        verbose_name = 'Account Role',
        validators=[MaxValueValidator(2), MinValueValidator(1)],
        blank=False,
    )
    
    # アイコン画像
    icon_path = models.CharField(
        verbose_name = 'アイコン画像パス',
        max_length = 255,
        null = True,
    )

    # 会社名
    company = models.CharField(
        verbose_name = 'Company',
        max_length=255,
        null=True,
    )

    # メールアドレス
    email = models.EmailField(
        verbose_name = 'Email',
        max_length = 255,
        unique = True,
    )

    # パスワード
    password = models.CharField(
        verbose_name = 'password',
        max_length = 255,
        blank=False,
        validators = [MinLengthValidator(8), MaxLengthValidator(30)],
    )

    # メールアドレス確認日時
    email_verified_at = models.DateTimeField(
        verbose_name = 'メールアドレス確認日',
        null=True,
    )

    # セッショントークン
    remember_token = models.CharField(
        verbose_name = 'トークン',
        max_length = 512,
        null = True,
    )

    # ユーザー作成日時
    created_at = models.DateTimeField(
        verbose_name = '作成日',
        default = timezone.now,
        null=True,
    )

    # ユーザー最終編集日時
    updated_at = models.DateTimeField(
        verbose_name = '更新日',
        null = True,
    )

    # ユーザー削除日時
    deleted_at = models.DateTimeField(
        verbose_name = '削除日',
        null = True,
    )

    #data_joined = models.DateTimeField(_('data joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    # メール送信メソッド
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)