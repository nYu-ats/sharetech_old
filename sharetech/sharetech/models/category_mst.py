from django.utils import timezone
from django.db import models

class CategoryMst(models.Model):
    '''
    相談窓口カテゴリマスタ
    '''

    class Meta:
        db_table = 'category_mst'
    
    """
    カラム定義

    default値
    null -> false
    blank -> false
    """

    # カテゴリ名
    category_name = models.CharField(
        verbose_name = 'カテゴリ名',
        max_length = 64,
    )

    # 親カテゴリID
    parent_category_id = models.PositiveIntegerField(
        verbose_name = '親カテゴリID',
        null = True,
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
