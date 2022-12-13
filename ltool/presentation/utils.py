from django.contrib.auth.models import User

from ltool.presentation.models import Documents


def get_documents(user: User = None) -> any:
    try:
        documents: Documents = Documents.objects.filter(user=user)
    except Exception:
        return False

    return documents
