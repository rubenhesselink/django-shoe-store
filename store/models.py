from django.db import models

from accounts.models import cUser


class Order(models.Model):
    user = models.ForeignKey(cUser, on_delete=models.CASCADE)
    shoe = models.ManyToManyField("Shoe")
    is_completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_completed = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)


class Shoe(models.Model):
    brand = models.CharField(max_length=50)
    name  = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    total_sales = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField("Category")
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['brand', 'name']

    def __str__(self):
        men = False
        women = False
        for cat in self.category.all():
            if 'Men' in cat.name:
                men = True
            if 'Women' in cat.name:
                women = True
        if men:
            return str(self.brand) + ' ' + str(self.name) + ' | Men'
        elif women:
            return str(self.brand) + ' ' + str(self.name) + ' | Women'
        else:
            return str(self.brand) + ' ' + str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name