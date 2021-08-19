from django.contrib import admin

from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_check', 'average_delivery_time')
    list_filter = ('name', 'average_check', 'average_delivery_time')
    search_fields = ('name',)
