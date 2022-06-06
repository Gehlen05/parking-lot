from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'plate', 'kind_choices')
