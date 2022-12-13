from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    form_class: AuthenticationForm = AuthenticationForm

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context: dict[str, any] = super().get_context_data(**kwargs)
        context["auth_page"] = True

        return context
