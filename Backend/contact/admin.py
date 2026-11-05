from django.contrib import admin
from .models import Contact, Career


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'company')
    search_fields = ('name', 'email', 'phone')


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'applied_at')
    search_fields = ('name', 'email')
    ordering = ('-applied_at',)