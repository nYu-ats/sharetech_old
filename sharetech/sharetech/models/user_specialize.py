from django.utils import timezone
from django.db import models
from .user import CustomUser

class UserSpecialize(models.Model):
    '''
    ユーザーの専門分野
    '''
    class Meta:
        db_table = 'user_specialize'
    
    '''
    カラム定義
    null -> false
    blank -> false
    '''

    # ユーザーID
    user_id = models.ForeignKey(
        'CustomUser',
        verbose_name = '申込者ID',
        on_delete = models.PROTECT,
    )

    # 専門分野
    specialize = models.CharField(
        verbose_name = '専門分野',
        max_length = 32,
    )

    # 論理削除フラグ
    id_deleted = models.BooleanField(
        verbose_name = 'Is Deleted',
        default = False,
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