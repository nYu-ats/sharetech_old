from django.utils import timezone
from django.db import models
from .consult_window import ConsultWindow
from .user import CustomUser

class ConsultApply(models.Model):
    '''
    申込履歴
    '''

    class Meta:
        db_table = 'consult_apply'
        constraints = [
            models.UniqueConstraint(
                fields = ['consult_window_id', 'user_id', 'apply_date'],
                name = 'apply_unique'
            )
        ]

    '''
    カラム定義

    default値
    null -> false
    blank -> false            
    '''

    # 相談窓口ID
    consult_window_id = models.ForeignKey(
        'ConsultWindow',
        verbose_name = '相談窓口ID',
        on_delete = models.PROTECT,
    )

    # ユーザーID
    user_id = models.ForeignKey(
        'CustomUser',
        verbose_name = '申込者ID',
        on_delete = models.PROTECT,
    )

    # 申込ステータス
    apply_status = models.PositiveSmallIntegerField(
        verbose_name = '申込ステータス',
        default = 1,
    )

    # 申込日
    apply_date = models.DateTimeField(
        verbose_name = '申込日',
        default = timezone.now,
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