from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(max_length=128, blank=True, null=True, default=None)
    short_description = models.TextField(max_length=100, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        s = "%s %s"
        return s % (self.name, self.id)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# Create your models here.
class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='static/media/product_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        s = "%s"
        return s % self.id

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
