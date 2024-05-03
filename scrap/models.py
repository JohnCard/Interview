from django.db import models
from selenium import webdriver
from bs4 import BeautifulSoup

# Create your models here.
class Vehicle(models.Model):
    owner = models.CharField(max_length=35)
    plaque = models.CharField(max_length=20)
    vin = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    sub_brand = models.CharField(max_length=20)
    verify_reason = models.CharField(max_length=30)
    service = models.CharField(max_length=15)
    line = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    no_tech = models.IntegerField()
    folio = models.IntegerField()    
