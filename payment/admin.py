from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'user', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('order__id', 'user__username')
