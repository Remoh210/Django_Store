from django.db import models
from products.models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        s = "%s"
        return s % self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comment = models.TextField(max_length=128, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        s = "Order_id: %s Status: %s"
        return s % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  #price mult number
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        s = "%s"
        return s % self.product.name

    class Meta:
        verbose_name = 'ProductInOrder'
        verbose_name_plural = 'ProductsInOrder'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.nmb * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


# def product_in_order_post_save(sender, instance, created, **kwargs ):
#     order = instance.order
#     all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
#
#     order_total_price = 0
#     for item in all_products_in_order:
#         order_total_price += item.total_price
#
#         instance.order.total_price = order_total_price
#         instance.order.save(force_update=True)
#
# post_save.connect(product_in_order_post_save, sender=ProductInOrder)


@receiver(post_save, sender=ProductInOrder)
def product_in_order_post_save(sender, instance, created, **kwargs ):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

        instance.order.total_price = order_total_price
        instance.order.save(force_update=True)