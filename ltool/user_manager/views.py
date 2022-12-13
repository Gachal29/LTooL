from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from ltool.presentation import utils as presentation_utils
from ltool.presentation.models import Documents
from ltool.user_manager import utils as user_manager_utils
from ltool.user_manager.models import Profile


class MypageView(LoginRequiredMixin, TemplateView):
    template_name: str = "user_manager/mypage.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context: dict[str, any] = super().get_context_data(**kwargs)

        user: User = self.request.user

        icon: Profile.icon = user_manager_utils.get_icon(user)
        context["icon"] = icon

        documents: Documents = presentation_utils.get_documents(user)
        context["documents"] = documents

        return context
