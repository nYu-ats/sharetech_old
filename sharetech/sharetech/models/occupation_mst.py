from django.utils import timezone
from django.db import models

class OccupationMst(models.Model):
    '''
    職種マスタモデル
    '''
    class Meta:
        db_table = 'occupation_mst'
    
    '''
    カラム定義
    null -> false
    blank -> false
    '''

    # 職種名
    name = models.CharField(
        verbose_name = 'Occupation Name',
        max_length = 64,
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