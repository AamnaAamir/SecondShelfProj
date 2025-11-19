# from django.urls import path
# from .views import add_user_wish, remove_wish_item, wish_list

# urlpatterns = [
#     path('wishlist', wish_list),
#     # path('user-wishlist', add_user_wish),
#     path('user-wishlist', add_user_wish, name='user-wishlist'),
#     path('remove-wishlist-item/<detail_id>', remove_wish_item), 
# ]

from django.urls import path
from .views import add_user_wish, remove_wish_item, wish_list

urlpatterns = [
    path('', wish_list, name='wish_list'),                 # /wishlist/
    path('user-wishlist/', add_user_wish, name='user-wishlist'),  # /wishlist/user-wishlist/
    # path('remove-wishlist-item/<detail_id>/', remove_wish_item),  # /wishlist/remove-wishlist-item/<id>/
]
