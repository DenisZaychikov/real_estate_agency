from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year',
                    'town', 'owners_phonenumber',
                    'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat_number']


@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    raw_id_fields = ['apartments']
