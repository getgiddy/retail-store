from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(default="product_images/default.png",
                              upload_to="product_images")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"product_id": self.pk})

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={"product_id": self.pk})


class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart-Item - {self.quantity} x {self.product} in {self.cart}"


ORDER_STATUSES = (
    ('nw', 'New'),
    ('ot', 'On Transit'),
    ('de', 'Delivered'),
    ('cc', 'Cancelled'),
)


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=ORDER_STATUSES, default='nw')
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s order"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Order-Item - {self.quantity} x {self.product} in {self.order}"
