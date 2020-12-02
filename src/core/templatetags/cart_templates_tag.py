from django import template

from core.models import Cart, CartItem

register = template.Library()


@register.filter()
def cart_items_count(user):
    # If user is authenticated and has a cart
    if user.is_authenticated and Cart.objects.filter(user=user).exists():
        # Get the count of the cartItems that belong to that cart
        return CartItem.objects.filter(cart=user.cart).count()
    else:
        # if not, count = 0
        return 0
