from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']