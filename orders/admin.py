from django.contrib import admin
from .models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'total_amount', 'status', 'order_date']
    list_filter = ['status', 'order_date']
    search_fields = ['user__username', 'status']

    class Meta:
        model = Order


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'book', 'quantity', 'price']
    list_filter = ['order']
    search_fields = ['book__title']

    class Meta:
        model = OrderDetail


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
