from django.db import models


class Products(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.Name


# class Cart(models.Model):
#     Items = models.ForeignKey(Products, on_delete=models.CASCADE)
#     total_products = models.IntegerField()

#     def __str__(self):
#         return self.total_products


# class Checkout(models.Model):
#     total_price = models.FloatField()

#     def __str__(self):
#         return self.total_products
