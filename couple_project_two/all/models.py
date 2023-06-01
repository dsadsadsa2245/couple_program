from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name='categories', null=True,
                                 on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.name}"

"""
from myapp.models import Category, Product

category = Category.objects.get(id=1)
products = Product.objects.filter(category=category)

for product in products:
    print(product.name, product.price)"""
