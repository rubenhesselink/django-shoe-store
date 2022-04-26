from django.contrib import admin

from . models import Order, Shoe, Category, ShoeColor

class ShoeColorInline(admin.StackedInline):
    model = ShoeColor


class ShoeAdmin(admin.ModelAdmin):
    inlines = [ShoeColorInline]

admin.site.register(Order)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Category)