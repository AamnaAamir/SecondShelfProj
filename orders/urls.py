from django.urls import path
from .views import checkout, order_history, order_detail

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('orders/', order_history, name='order_history'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
]
