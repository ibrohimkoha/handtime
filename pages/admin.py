from django.contrib import admin
from .models import WatchModel, Category
# Register your models here.
@admin.register(WatchModel)
class WatchModelAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'price', 'aksiya_price')

    search_fields = ( 'name', 'price', 'aksiya_price')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
    