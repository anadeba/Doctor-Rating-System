### Collect link of all Doctors and Hospitals/Clinics

### Import libraries
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Launch Firefox driver - Selenium

binary = FirefoxBinary( 'C:\Program Files (x86)\Mozilla Firefox\\firefox.exe' )
driver1 = webdriver.Firefox( firefox_binary=binary )

doc_links = []
hospital_links = []

### Link collection

### Read Links using BeautifulSoup

for specialist in ("gynecologist-obstetrician","ear-nose-throat-ent-specialist"):
    for place in ("bangalore", "chennai", "mumbai", "kolkata", "delhi"):
        for pg in range( 1, 30 ):
            url = 'https://www.practo.com/%s/%s?page=%d' % (place, specialist, pg)
            driver1.get( url )
            html_page = driver1.page_source.encode( 'utf-8' )
            soup = BeautifulSoup( html_page, "html.parser" )
            for ln in (soup.find_all( "a", class_="link doc-name smokeliftDoctorLink fm-target" )):
                doc_links.append(ln['href'])
            for ln in (soup.find_all( "a", class_="link doc-name adClinicProfileLink smokeliftClinicLink" )):
                hospital_links.append(ln['href'])
            print specialist,place,pg
            if soup.find(rel="next") == None:
                break

### Save output to excel

doclinks = pd.DataFrame({'doctor_links':doc_links})
hospitallinks = pd.DataFrame({'hospital_links':hospital_links})
doclinks.to_excel('C:\\Users\\debanjan\\Desktop\\doctor_links.xlsx','Sheet1')
hospitallinks.to_excel('C:\\Users\debanjan\\Desktop\\hospital_links.xlsx','Sheet1')
