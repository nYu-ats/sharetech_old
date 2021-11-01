from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.db import models
from . import Article

class Chapter(models.Model):
    class Meta:
        db_table = 'chapters'
    
    """
    カラム定義

    default値
    null -> false
    blank -> false
    """
    # 記事のインデックス
    chapter_idx = models.PositiveIntegerField(
        verbose_name = 'Chapter Index',
        validators = [MaxValueValidator(3), MinValueValidator(1)],
    )

    article_id = models.ForeignKey(
        'Article',
        verbose_name = 'Article ID',
        on_delete = models.CASCADE,
    )

    img_path = models.CharField(
        verbose_name = 'Image Path',
        max_length = 255,
    )

    sentence = models.CharField(
        verbose_name = 'Sentence',
        max_length = 255,
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