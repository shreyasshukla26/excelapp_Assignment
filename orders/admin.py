from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Order

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('order_id', 'product_name', 'product_price', 'shipped')
    

