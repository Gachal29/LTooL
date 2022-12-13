from django import forms

# from django.contrib.auth.models import User
# from ltool.user_manager.models import Profile, ScrapboxProjects


class EditProfileForm(forms.Form):
    first_name: forms.CharField = forms.CharField(max_length=150, blank=True)
    last_name: forms.CharField = forms.CharField(max_length=150, blank=True)
