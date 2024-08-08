from django.contrib import admin
from .models import Bookings, LikedProduct

class BookingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'product_price')
    list_filter = ('user', 'product__name')

    def product_name(self, obj):
        return obj.product.name if obj.product else 'No Product'
    product_name.admin_order_field = 'product__name'
    product_name.short_description = 'Product Name'

    def product_price(self, obj):
        return obj.product.price if obj.product else 'N/A'
    product_price.admin_order_field = 'product__price'
    product_price.short_description = 'Product Price'

class LikedProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name')
    list_filter = ('user', 'product__name')

    def product_name(self, obj):
        return obj.product.name
    product_name.admin_order_field = 'product__name'
    product_name.short_description = 'Product Name'

admin.site.register(Bookings, BookingsAdmin)
admin.site.register(LikedProduct, LikedProductAdmin)
