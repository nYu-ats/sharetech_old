from django.utils import timezone
from django.db import models
from .user import CustomUser

class ConsultWindow(models.Model):
    '''
    相談窓口モデル
    '''
    class Meta:
        db_table = 'consult_window'
    
    '''
    カラム定義
    null,false項目未指定の場合
     null -> false
     blank -> false
    '''

    # 専門家ユーザーid
    expert_user_id = models.ForeignKey(
        'CustomUser',
        verbose_name = '専門家ユーザーID',
        on_delete = models.CASCADE,
    )

    # 相談窓口タイトル
    consult_window_title = models.CharField(
        verbose_name = '相談窓口タイトル',
        max_length = 128,
    )

    # 相談窓口概要
    consult_window_overview = models.CharField(
        verbose_name = '相談窓口概要',
        max_length = 512,
    )

    # 相談料金
    consult_price = models.PositiveIntegerField(
        verbose_name = '相談料金',
        default = 0,
    )

    # Scheduler URL
    scheduler_url = models.CharField(
        verbose_name = 'Scheduler URL',
        max_length = 512,
    )

    # 実績
    archivement = models.CharField(
        verbose_name = '実績',
        max_length = 512,
    )

    # 閲覧数
    viewed_num = models.PositiveIntegerField(
        verbose_name = '閲覧数',
        default = 0,
    )

    # 申込数
    applyed_num = models.PositiveIntegerField(
        verbose_name = '申込数',
        default = 0,
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