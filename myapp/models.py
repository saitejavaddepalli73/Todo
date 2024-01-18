from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


# class Customer(models.Model):
#     firstname=models.CharField(max_length=50)
#     lastname=models.CharField(max_length=50)
#     email=models.EmailField(max_length=50)
#     password=models.CharField(max_length=50)

class Description(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

def __str__(self):
    return self.user.username