from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.mobile

class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.FloatField()
    class Meta:
        db_table='Product_Info'

    def __str__(self):
        return self.name












