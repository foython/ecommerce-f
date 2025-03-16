from django.contrib import admin
from .models import Cart

# Register your models here.
@admin.register(Cart)
class ProductAdmin(admin.ModelAdmin): 
    list_display = [ 'id','session', 'product', 'size', 'quantity', 'total']
