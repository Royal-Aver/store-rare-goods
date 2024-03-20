from email.policy import default
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="products_images", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"

    def __str__(self):
        return f'{self.name} | {self.quantity} | {self.category}'