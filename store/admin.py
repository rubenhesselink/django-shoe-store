from django.contrib import admin

from . models import Order, Shoe, Category

admin.site.register(Order)
admin.site.register(Shoe)
admin.site.register(Category)