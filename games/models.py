from django.db import models
from django.forms import ModelForm

class Review(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  review = models.CharField(max_length=255)
