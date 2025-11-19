from django.urls import path
from . import views

urlpatterns = [
    path('options/<int:order_id>/', views.payment_options, name='payment_options'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
