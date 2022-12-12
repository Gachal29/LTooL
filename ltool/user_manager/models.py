from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)

    view_name: models.CharField = models.CharField(max_length=150, verbose_name="表示名")
    icon: models.ImageField = models.ImageField(upload_to="icons", blank=True, verbose_name="アイコン")
    introduction: models.CharField = models.CharField(max_length=1024, blank=True, verbose_name="自己紹介")

    def __str__(self) -> str:
        return f"id:{self.id}, user:{self.user}"

    class Meta:
        verbose_name_plural: str = "プロフィール"


class ScrapboxProjects(models.Model):
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    project: models.CharField = models.CharField(max_length=25, verbose_name="プロジェクト")

    def __str__(self) -> str:
        return f"id:{self.id} user:{self.user} project:{self.project}"

    class Meta:
        verbose_name_plural: str = "Scrapboxプロジェクト"
