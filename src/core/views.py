from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.models import Cart, CartItem, Product


def index(request):
    user_cart_items = None
    if request.user.is_authenticated and Cart.objects.filter(user=request.user).exists():
        user_cart_items = CartItem.objects.filter(cart=request.user.cart)

    sub_total = 0.0
    if user_cart_items:
        for cart_item in user_cart_items:
            sub_total += cart_item.get_total()

    context = {
        'products': Product.objects.all(),
        'cart_items': user_cart_items,
        'sub_total': sub_total,
    }
    return render(request, 'index.html', context)


def product_detail(request, product_id):
    context = {
        # 'product': Product.objects.get(id=product_id)
        'product': get_object_or_404(Product, pk=product_id)
    }

    return render(request, "product.html", context)


@login_required
def add_to_cart(request, product_id):
    # Get the product to be added to cart
    product = get_object_or_404(Product, pk=product_id)
    cart = None
    # Check if user has a cart
    if Cart.objects.filter(user=request.user).exists():
        # if yes, continue
        cart = Cart.objects.get(user=request.user)
    else:
        # if no, Create cart and then continue
        cart = Cart.objects.create(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    # Check if user's cart has cartItem with this product
    if cart_items.filter(product=product).exists():
        # If yes, increment the quantity of that cartItem
        cart_item = cart_items.get(product=product)
        cart_item.quantity += 1
        cart_item.save()
    else:
        # If no, create cartItem with that product
        CartItem.objects.create(cart=cart, product=product)

    return redirect(reverse('home'))


@login_required
def remove_from_cart(request, cart_item_id):
    # Get the cart item
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    # and delete cart item
    cart_item.delete()

    return redirect(reverse('home'))

@login_required
def cart(request):
    return render(request, "cart.html")
