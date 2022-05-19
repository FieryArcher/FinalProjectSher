from django.contrib import admin
from .models import *

admin.site.register(Food)

admin.site.register(Chef)
admin.site.register(Suppliers)
admin.site.register(Clients)
admin.site.register(Order)
admin.site.register(Waiter)
admin.site.register(IngredientsForBurger)
admin.site.register(Provide)

