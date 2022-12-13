from django.contrib.auth.models import User

from ltool.user_manager.models import Profile


def get_icon(user: User = None) -> any:
    try:
        profile: Profile = Profile.objects.get(user=user)
    except Exception:
        return False

    icon: Profile.icon = profile.icon

    return icon
