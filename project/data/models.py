from django.contrib.admin import options
from django.contrib.auth.models import User
from django.db import models
import random


class Chef(models.Model):
    id = models.IntegerField(primary_key=True)
    chef_name = models.CharField(max_length=100)
    chef_price = models.IntegerField()

    def __str__(self):
        return self.chef_name


class Food(models.Model):
    food_name = models.CharField(max_length=100)
    price = models.IntegerField()
    food_description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="img/%y", null=True, blank=True, default='default.jpg')
    chef_id = models.ForeignKey(Chef, related_name='ch2', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.food_name


class Suppliers(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    supplier_city = models.CharField(max_length=100)
    supplier_phone = models.IntegerField()
    supplier_price = models.IntegerField()
    supplier_chef_id = models.ForeignKey(Chef, related_name='su2', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.supplier_name



class Waiter(models.Model):
    waiter_id = models.IntegerField(primary_key=True)
    waiter_name = models.CharField(max_length=100)
    waiter_price = models.IntegerField()
    waiter_phone = models.IntegerField()
    image = models.ImageField(upload_to="img/%y", null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.waiter_name


# class Client(models.Model):
#     customer_name = models.CharField(primary_key=True, max_length=100)
#     customer_address = models.CharField(max_length=100)
#     customer_phone = models.IntegerField()
#     customer_waiter_id = models.ForeignKey(Waiter,related_name='customer', on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return self.customer_name

class Clients(models.Model):
    client_name = models.CharField(primary_key=True, max_length=100)
    client_address = models.CharField(max_length=100)
    client_phone = models.IntegerField()
    waiter_id = models.ForeignKey(Waiter, related_name='customer', on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.client_name
    class Meta:
        verbose_name = 'Client'


class Order(models.Model):
    orders_id = models.CharField(max_length=100)
    orders_name = models.ForeignKey(Clients, related_name='order', on_delete=models.DO_NOTHING)
    orders_food = models.ForeignKey(Food, related_name='food', on_delete=models.DO_NOTHING)
    data = models.DateField()

    def __str__(self):
        return self.orders_id




class IngredientsForBurger(models.Model):
    ingredients_id = models.IntegerField()
    ingredients_name = models.CharField(max_length=100,primary_key=True)
    ingredients_img = models.ImageField(upload_to="img/%y", null=True, blank=True, default='default.jpg')
    ingredients_validity = models.DateField()
    ingredients_food_id = models.ForeignKey(Food, related_name='ingredients', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ingredients_name


class Provide(models.Model):
    provides_id = models.CharField(max_length=100,primary_key=True)
    provides_supplier_id = models.ForeignKey(Suppliers, related_name='provides', on_delete=models.DO_NOTHING)
    provides_ingredients_name = models.ForeignKey(IngredientsForBurger, related_name='Ingredients_name', on_delete=models.DO_NOTHING)
    provides_number = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return self.provides_id


