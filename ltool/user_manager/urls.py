from django.urls import path

from ltool.user_manager.views import MypageView, ProfileView

urlpatterns: list[path] = [
    path("", MypageView.as_view(), name="mypage"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
