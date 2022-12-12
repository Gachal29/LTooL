from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Settings(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)

    document_public: models.BooleanField = models.BooleanField(default=True, verbose_name="資料公開")
    schedule_public: models.BooleanField = models.BooleanField(default=True, verbose_name="スケジュール公開")

    insert_page: models.BooleanField = models.BooleanField(default=True, verbose_name="ページ数の表示")

    time_keeper: models.BooleanField = models.BooleanField(default=True, verbose_name="定期タイムキーパー")
    time_keeper_interval: models.IntegerField = models.IntegerField(default=1, verbose_name="定期通知間隔")

    finish_keeper: models.BooleanField = models.BooleanField(default=True, verbose_name="終了前タイムキーパー")
    finish_keeper_start: models.IntegerField = models.IntegerField(default=30, verbose_name="終了前通知スタート時間")
    finish_keeper_interval: models.IntegerField = models.IntegerField(default=10, verbose_name="終了前通知間隔")

    def __str__(self) -> str:
        return f"id:{self.id} user:{self.user}"

    class Meta:
        verbose_name_plural: str = "個人設定"


class Documents(models.Model):
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)

    title: models.CharField = models.CharField(max_length=256, verbose_name="タイトル")
    file: models.FileField = models.FileField(upload_to="documents/%Y/%m/%d", verbose_name="資料")
    created_date: models.DateTimeField = models.DateTimeField(default=timezone.now, verbose_name="作成日")

    def __str__(self) -> str:
        return f"id:{self.id}, title:{self.title}"

    class Meta:
        verbose_name_plural: str = "作成した資料"


MYSELF_PAGE_NAME_CHOICES: list[tuple[int, str]] = [
    (1, "full_name"),
    (2, "view_name"),
    (3, "username")
]

class MyselfPage(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)

    insert_name: models.IntegerField = models.IntegerField(choices=MYSELF_PAGE_NAME_CHOICES, verbose_name="記載する名前")
    insert_icon: models.BooleanField = models.BooleanField(default=True, verbose_name="アイコンを表示")

    file: models.FileField = models.FileField(upload_to="documents/myself", verbose_name="自己紹介ファイル")

    def __str__(self) -> str:
        return f"id:{self.id}, user:{self.user}"

    class Meta:
        verbose_name_plural: str = "自己紹介ページ"
