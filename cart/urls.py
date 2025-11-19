# from django.urls import path
# from .views import add_to_cart, update_cart, view_cart, remove_from_cart

# urlpatterns = [
#     path('cart/', view_cart, name='view_cart'),
#     path('cart/add/', add_to_cart, name='add_to_cart'),
#     path('cart/update/', update_cart, name='update_cart'),
#     path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('update/', views.update_cart, name='update_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('cart-size/', views.cart_size, name='cart_size'),
]
