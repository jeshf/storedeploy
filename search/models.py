from django.db import models

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=True, default='')
    price = models.FloatField()
    quantity = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
    # Create your models here.