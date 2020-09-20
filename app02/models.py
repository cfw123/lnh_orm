from django.db import models

# Create your models here.


class Food(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2,default=100)