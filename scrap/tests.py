from django.test import TestCase
# Create your tests here
from .models import Vehicle
from selenium import webdriver
from bs4 import BeautifulSoup

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