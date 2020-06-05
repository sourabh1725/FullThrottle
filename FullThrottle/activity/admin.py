"""
Registering model Activity period
"""
from django.contrib import admin
from .models import ActivityPeriod


class ActivityAdmin(admin.ModelAdmin):
    pass


admin.site.register(ActivityPeriod, ActivityAdmin)
