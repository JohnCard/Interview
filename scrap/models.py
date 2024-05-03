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

# This a function to go the url and download all data for an specific vehicle user

def get_data(link):
    driver = webdriver.Chrome()
    driver.get(link)
    soup = BeautifulSoup(driver.page_source,'lxml')
    
    def return_value(clas,num):
        return soup.find_all('div',class_=clas)[num].text   
    
    owner = return_value('fw-bold text-gray-800 fs-6',0)
    plaque = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',0)
    vin = return_value('fw-bold text-gray-800 fs-6',1)
    brand = return_value('fw-bold text-gray-800 fs-6',2)
    sub_brand = return_value('fw-bold text-gray-800 fs-6',3)
    verify_reason = return_value('fw-bold text-gray-800 fs-6',4)
    service = return_value('fw-bold text-gray-800 fs-6',5)
    line = return_value('fw-bold text-gray-800 fs-6',6)
    no_tech = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',4)
    folio = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',4)
    
    Vehicle.objects.create(owner=owner,plaque=plaque, vin=vin,brand=brand,sub_brand=sub_brand,verify_reason=verify_reason,
    service=service,line=line,no_tech=no_tech,folio=folio)
    
    driver.close()
    
