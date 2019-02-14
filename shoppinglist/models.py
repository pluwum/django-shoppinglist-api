from django.db import models

# Create your models here.


class ShoppingList(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class ShoppingListItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    shoppinglist = models.ForeignKey(
        ShoppingList, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
