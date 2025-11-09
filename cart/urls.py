from django.urls import path
from .views import add_to_cart, update_cart, view_cart, remove_from_cart

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/update/', update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
