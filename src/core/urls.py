from django.urls import path
from core.views import index, product_detail, add_to_cart, remove_from_cart

urlpatterns = [
    path('', index, name='home'),
    path('cart/', index, name='cart'),
    path("products/<int:product_id>/", product_detail, name="product-detail"),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:cart_item_id>/", remove_from_cart, name="remove_from_cart"),
]
