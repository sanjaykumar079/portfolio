from django.db import models
from django.contrib import admin
# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  subject = models.CharField(max_length=50)
  message = models.TextField()
  def __str__(self):
     return f"{self.name} + 'sanjay'" 