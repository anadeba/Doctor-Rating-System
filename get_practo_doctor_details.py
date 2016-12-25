### Get details for each Doctor links

import pandas as pd
import xlrd
import numpy as np
import re
import sys
import time
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

reload(sys)
sys.setdefaultencoding('utf-8')

doctor_details = pd.DataFrame()

binary = FirefoxBinary( 'C:\Program Files (x86)\Mozilla Firefox\\firefox.exe' )
driver1 = webdriver.Firefox( firefox_binary=binary )

doc_links = pd.read_excel('X:\\ISB\\Course\\Term1\\Visit2\\Practicum\\doctor_links.xlsx',sheetname='Sheet1')

### For each doctor links get doctor details

for url in (doc_links.doctor_links):
    global doctor_details
    driver1.get(url)
    time.sleep(10)
    try:
        driver1.find_element_by_id( "reviewsNavLink" ).click( )
        time.sleep( 10 )
        print "ok1"
        while 1:
            print "here"
            driver1.find_elements_by_css_selector(".recommended-next-page")[0].click()
            time.sleep( 4 )
            print "ok2"
    except (NoSuchElementException,ElementNotVisibleException,IndexError):
        pass

    html_page = driver1.page_source
    soup = BeautifulSoup( html_page, "html.parser" )
    Name = soup.find(itemprop = "name").text

    Qualification = re.split(',',re.sub("\s+"," ",soup.find( "p", class_="doctor-qualifications" ).text.encode('ascii', 'ignore')))

    Speciality = re.split(",",re.sub("\s+"," ",soup.find("h2", class_ = "doctor-specialties").text.encode('ascii', 'ignore')))

    Experience = re.findall("\d+", Speciality[-1])[0]
    del Speciality[-1]

    Award = []
    for x in soup.find_all(itemprop="award"):
        Award.append(re.sub("\s+"," ",x.text.encode('ascii', 'ignore')))

    Reviews = []
    for x in soup.find_all("span", class_ = "less-review"):
        Reviews.append(re.sub("\s+"," ",x.text.encode('ascii', 'ignore')))
    Number_of_Reviews = len(Reviews)

    try:
        Likes = re.findall("\d+%",soup.find("div", class_ = "patient_experience_score recommend").text.encode('ascii', 'ignore'))
        Likes = re.sub("\%","",Likes[0])
        Votes = re.findall("\(\d+",soup.find("div", class_ = "patient_experience_score recommend").text.encode('ascii', 'ignore'))
        Votes = re.sub("\(","",Votes[0])
    except (AttributeError):
        Likes = 0
        Votes = 0

    Location = soup.input['value']

    print Name, Qualification, Speciality ,Experience, Likes, Votes, Location, Award, Reviews, Number_of_Reviews

    doctor_details = doctor_details.append({

        'Name': Name,
        'Qualification': Qualification,
        'Speciality': Speciality,
        'Experience': Experience,
        'Likes': Likes,
        'Votes': Votes,
        'Location': Location,
        'Award': Award,
        'Reviews': Reviews,
        'Number_of_Reviews': Number_of_Reviews

    }, ignore_index= True)
    doctor_details.to_excel( 'X:\\ISB\\Course\\Term1\\Visit2\\Practicum\\doctor-details.xlsx', 'Sheet1',columns=['Name','Qualification','Speciality','Experience','Likes','Votes','Location','Award','Reviews','Number_of_Reviews'] )

### Save doctor details
doctor_details.to_excel('X:\\ISB\\Course\\Term1\\Visit2\\Practicum\\doctor-details.xlsx','Sheet1')









