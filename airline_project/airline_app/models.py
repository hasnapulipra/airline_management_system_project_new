from django.db import models
 
# Create your models here
class Customer(models.Model):
    fullname = models.TextField(max_length=50)
    username = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    contact = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='pictures/')
    gender = models.TextField(max_length=50)

class Request(models.Model):
    name = models.TextField(max_length=50)
    username = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    contact = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    country = models.TextField(max_length=50)
    image = models.ImageField(upload_to='pictures/')