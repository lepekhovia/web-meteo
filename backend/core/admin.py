from django.contrib import admin
from core.models.user import User
from core.models.request_history import RequestHistory


admin.site.register(User)
admin.site.register(RequestHistory)
