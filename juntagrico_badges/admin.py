from django.contrib import admin
from juntagrico.admins import BaseAdmin

from juntagrico_badges.entity.badges import Badge


class BadgeAdmin(BaseAdmin):
    filter_horizontal = ['members']
    list_display = ['name', 'self_assignable']


admin.site.register(Badge, BadgeAdmin)
