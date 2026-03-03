from django.contrib import admin

from .models import Notification, Owner

admin.site.register(Owner)
admin.site.register(Notification)
