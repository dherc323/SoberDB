from django.db import models
from django.urls import reverse
from django.forms import ModelForm, Textarea

# Create your models here:
class Lab_Item(models.Model):
    Item_name = models.CharField(max_length=200)
    Item_brand = models.CharField(max_length=100, null = True)
    Room = models.CharField(max_length=200)
    Amount = models.IntegerField()

def get_absolute_url(self):
    return reverse('Inventory:index', kwargs={'pk':self.pk})

def __str__(self):
    return (self.Item_name + ";" +self.Amount)
