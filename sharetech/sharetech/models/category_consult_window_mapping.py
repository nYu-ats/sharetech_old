from django.utils import timezone
from django.db import models
from .consult_window import ConsultWindow
from .category_mst import CategoryMst

class CategoryConsultWindowMapping(models.Model):
    '''
    カテゴリと相談窓口のマッピング
    '''

    class Meta:
        db_table = 'category_consult_window_mapping'
        constraints = [
            models.UniqueConstraint(
                fields = ['category_id', 'consult_window_id'],
                name = 'mapping_unique'
            )
        ]

    '''
    カラム定義

    default値
    null -> false
    blank -> false
    '''

    # カテゴリID
    category_id = models.ForeignKey(
        'CategoryMst',
        verbose_name = 'カテゴリID',
        on_delete = models.CASCADE,
        default = 99,
    )

    # 相談窓口ID
    consult_window_id = models.ForeignKey(
        'ConsultWindow',
        verbose_name = '相談窓口ID',
        on_delete = models.CASCADE,
    )
    
    # 論理削除フラグ
    is_deleted = models.BooleanField(
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