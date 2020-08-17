from django.db import models

# Create your models here.

class items(models.Model):
    itemname=models.CharField(max_length=200)
    quantity=models.CharField(max_length=20)
    rate=models.IntegerField()
