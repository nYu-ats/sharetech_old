from django.core.validators import MaxLengthValidator, MinLengthValidator,MaxValueValidator, MinValueValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from .industry_mst import IndustryMst
from .position_mst import PositionMst
from .occupation_mst import OccupationMst

# ユーザーマネージャカスタム
class CustomUserManager(BaseUserManager):
    """
    カスタムユーザーマネージャー
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
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    カスタムユーザーモデル
    
    """

    class Meta:
        db_table = 'user'
    
    username_validator = UnicodeUsernameValidator()
    objects = CustomUserManager()
    roleChoices = (
        ('1', '専門家'),
        ('2', '一般' )
    )

    """
    カラム定義

    default値
    null -> false
    blank -> false
    """
    # ユーザー日本語名前
    first_name_jp = models.CharField(
        verbose_name = 'First Name Japanese',
        help_text='必須項目です。全角文字で20文字以下にしてください。',
        max_length = 20,
        validators=[username_validator],
    )

    # ユーザー日本語名字
    family_name_jp = models.CharField(
        verbose_name = 'Family Name Japanese',
        help_text='必須項目です。全角文字で20文字以下にしてください。',
        max_length = 20,
        validators=[username_validator],
    )

    # ユーザー英語名前
    first_name_en = models.CharField(
        verbose_name = 'First Name Englist',
        help_text='必須項目です。全角文字で20文字以下にしてください。',
        max_length = 20,
        validators=[username_validator],
    )

    # ユーザー英語名字
    family_name_en = models.CharField(
        verbose_name = 'Family Name Englist',
        help_text='必須項目です。全角文字で20文字以下にしてください。',
        max_length = 20,
        validators=[username_validator],
    )

    # ユーザー名
    username_kana = models.CharField(
        verbose_name = 'Name Kana',
        help_text='必須項目です。全角文字で50文字以下にしてください。',
        max_length = 64,
        validators=[username_validator],
    )

    # 権限
    role_code = models.CharField(
        verbose_name = 'Account Role',
        max_length = 1,
        choices = roleChoices,
    )
    
    # アイコン画像
    icon_path = models.CharField(
        verbose_name = 'Icon Image Path',
        max_length = 512,
        null = True,
    )

    # 自己紹介文
    introduction = models.CharField(
        verbose_name = 'Introduction',
        max_length = 512,
        null = True,
    )

    # 会社名
    company = models.CharField(
        verbose_name = 'Company',
        max_length=256,
    )

    # メールアドレス
    email = models.EmailField(
        verbose_name = 'Email',
        max_length = 256,
        unique = True,
    )

    # メールアドレス変更用一時格納場所
    tmp_email = models.EmailField(
        verbose_name = 'Tmp Email',
        max_length = 256,
        null = True,
    )

    # 業種ID
    industry_id = models.ForeignKey(
        'IndustryMst',
        verbose_name = 'Industry ID',
        on_delete = models.SET_NULL,
        null = True,
    )

    # 職種ID
    occupation_id = models.ForeignKey(
        'OccupationMst',
        verbose_name = 'Occupation ID',
        on_delete = models.SET_NULL,
        null = True,
    )

    # 役職ID
    position_id = models.ForeignKey(
        'PositionMst',
        verbose_name = 'Position ID',
        on_delete = models.SET_NULL,
        null = True,
    )

    # 生年月日
    birthday = models.DateField(
        verbose_name = 'Birthday',
        null = True,
    )

    # パスワード
    password = models.CharField(
        verbose_name = 'password',
        max_length = 255,
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

    # 論理削除フラグ
    is_deleted = models.BooleanField(
        verbose_name = 'Is Deleted',
        default = False,
    )

    # ログインカウンター
    login_counter = models.PositiveIntegerField(
        verbose_name = 'Login Counter',
        default = 0
    )

    # 作成日時
    created_at = models.DateTimeField(
        verbose_name = 'Create Date',
        default = timezone.now,
    )

    # 最終編集日時
    updated_at = models.DateTimeField(
        verbose_name = 'Update Date',
        null = True,
    )

    # 削除日時
    deleted_at = models.DateTimeField(
        verbose_name = 'Delete Date',
        null = True,
    )

    # get_email_filed_name()で返される値
    EMAIL_FIELD = 'email'
    # ユーザーを一意に特定する値
    USERNAME_FIELD = 'email'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)