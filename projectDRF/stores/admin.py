from django.contrib import admin

# Register your models here.
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'rating', 'owner', 'status']
    search_fields = ['name', 'description', 'rating', 'owner', 'status']
    list_filter = ['name', 'description', 'rating', 'owner', 'status']
    list_editable = ['rating']

    class Meta:
        model = Store


admin.site.register(Store, StoreAdmin)
