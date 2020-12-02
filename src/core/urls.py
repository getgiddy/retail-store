from django.urls import path
from core.views import index, product_detail, add_to_cart

urlpatterns = [
    path('', index, name='home'),
    path("products/<int:product_id>/", product_detail, name="product-detail"),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart")
]
