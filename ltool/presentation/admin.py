from django.contrib import admin

from ltool.presentation.models import Documents, MyselfPage, Settings

admin.site.register(Settings)
admin.site.register(Documents)
admin.site.register(MyselfPage)
