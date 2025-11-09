from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'created_at']
    search_fields = ['user__username']

    class Meta:
        model = Cart

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'cart', 'book', 'quantity', 'price']
    list_filter = ['cart']
    search_fields = ['book__title']

    class Meta:
        model = CartItem

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
