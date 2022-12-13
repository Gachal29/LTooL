from django.urls import path

from ltool.user_manager.views import MypageView

urlpatterns: list[path] = [
    path("", MypageView.as_view(), name="mypage"),
]
