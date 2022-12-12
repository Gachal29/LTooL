from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    form_class: AuthenticationForm = AuthenticationForm
