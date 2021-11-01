from django.utils import timezone
from django.db import models
from . import User

class Article(models.Model):
    class Meta:
        db_table = 'articles'
    
    """
    カラム定義

    default値
    null -> false
    blank -> false
    """
    # 記事のタイトル
    title = models.CharField(
        verbose_name = 'Title',
        max_length = 255,
    )

    # アイキャッチ画像パス
    # TODO 【確認】暫定で記事の1枚目画像を指定しているが、別でアップさせるか
    eyecatch_path = models.CharField(
        verbose_name = 'Eyecatch Path',
        max_length = 255,    
    )

    # 投稿者のユーザーID(外部キー)
    contributor_id = models.ForeignKey(
        'User',
        verbose_name = 'Contributor',
        on_delete = models.CASCADE,
    )

    # 閲覧数(集計列)
    viewed_count = models.PositiveIntegerField(
        verbose_name = 'Viewed Count',
        default = 0,
    )

    # お気に入り数(集計列)
    favorite_count = models.PositiveIntegerField(
        verbose_name = 'Favorite Count',
        default = 0,
    )

    # 記事作成日時
    created_at = models.DateTimeField(
        verbose_name = 'Create Date',
        default = timezone.now,
        null=True,
    )

    # 記事最終編集日時
    updated_at = models.DateTimeField(
        verbose_name = 'Update Date',
        null = True,
    )

    # 記事削除日時
    deleted_at = models.DateTimeField(
        verbose_name = 'Delete Date',
        null = True,
    )

