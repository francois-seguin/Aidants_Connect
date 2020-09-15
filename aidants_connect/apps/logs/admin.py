from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Journal


class JournalAdmin(ModelAdmin):
    list_display = ("id", "action", "aidant", "creation_date")
    list_filter = ("action",)
    search_fields = ("action", "aidant")
    ordering = ("-creation_date",)


admin.site.register(Journal, JournalAdmin)
