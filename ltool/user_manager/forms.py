from django import forms

# from django.contrib.auth.models import User
# from ltool.user_manager.models import Profile, ScrapboxProjects


class EditProfileForm(forms.Form):
    first_name: forms.CharField = forms.CharField(max_length=150, required=False)
    last_name: forms.CharField = forms.CharField(max_length=150, required=False)

    view_name: forms.CharField = forms.CharField(max_length=150, required=False, label="表示名")
    icon: forms.ImageField = forms.ImageField(required=False, label="アイコン")
    introduction: forms.CharField = forms.CharField(max_length=1024, required=False, label="自己紹介")
