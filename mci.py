### Scrape Medical Council of India

import time
import thread
import sys
from threading import Thread
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

reload(sys)
sys.setdefaultencoding('utf-8')

Medical_Council = "ASS"
doc_list = pd.DataFrame()

started1 = 1
started2 = 1
started3 = 1
started4 = 1
started5 = 1
started6 = 1
started7 = 1
started8 = 1
started9 = 1
started10 = 1
started11 = 1
started12 = 1

def read(driver_name,drivern):
    global doc_list
    while 1:
        lst = len(drivern.find_elements_by_css_selector("#lnkDesc span"))
        print lst, driver_name
        for wndw in range(0, lst):
            print wndw, driver_name
            drivern.find_elements_by_css_selector("#lnkDesc span")[wndw].click()
            time.sleep(2.5)
            drivern.switch_to.window(drivern.window_handles[1])
            html_source = drivern.page_source.encode('utf-8')
            soup = BeautifulSoup(html_source, "html.parser")

            while html_source is None:
                print "Read failed with AttributeError: 'NoneType' object has no attribute 'text', retrying ....."
                html_source = drivern.page_source.encode('utf-8')

            try:
                Name = soup.find(id="Name").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Name"
                Name = np.NaN
            try:
                FatherName = soup.find(id="FatherName").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Father's name"
                FatherName = np.NaN
            try:
                DOB = soup.find(id="DOB").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at DOB"
                DOB = np.NaN
            try:
                YearInfo = soup.find(id="lbl_Info").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Year of Information"
                YearInfo = np.NaN
            try:
                RegNo = soup.find(id="Regis_no").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Registration No."
                RegNo = np.NaN
            try:
                RegDate = soup.find( id="Date_Reg" ).text
            except (NoSuchElementException, TimeoutException, AttributeError):
                RegDate = np.NaN
            try:
                MedicalCouncil = soup.find(id="Lbl_Council").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Date of Registration"
                MedicalCouncil = np.NaN
            try:
                Qualification = soup.find(id="Qual").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Qualification"
                Qualification = np.NaN
            try:
                QualificationYear = soup.find(id="QualYear").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Qualification Year"
                QualificationYear = np.NaN
            try:
                University = soup.find(id="Univ").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at University"
                University = np.NaN
            try:
                Address = soup.find(id="Address").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Address"
                Address = np.NaN
            try:
                AddQual1 = soup.find(id="AddQual1").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Additional Qualification 1"
                AddQual1 = np.NaN
            try:
                AddQualYear1 = soup.find(id="AddQualYear1").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Additional Qualification Year 1"
                AddQualYear1 = np.NaN
            try:
                AddQualUniv1 = soup.find(id="AddQualUniv1").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Additional Qualification University 1"
                AddQualUniv1 = np.NaN
            try:
                AddQual2 = soup.find(id="AddQual2").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Additional Qualification 2"
                AddQual2 = np.NaN
            try:
                AddQualYear2 = soup.find(id="AddQualYear2").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Additional Qualification Year 2"
                AddQualYear2 = np.NaN
            try:
                AddQualUniv2 = soup.find(id="AddQualUniv2").text
            except (NoSuchElementException, TimeoutException, AttributeError):
                print "Got exception at Additional Qualification University 2"
                AddQualUniv2 = np.NaN

            doc_list = doc_list.append(
                {'Name': Name, 'FatherName': FatherName,
                 'DOB': DOB, 'YearInfo': YearInfo,
                 'RegNo': RegNo, 'RegDate': RegDate,
                 'MedicalCouncil': MedicalCouncil, 'Qualification': Qualification,
                 'QualificationYear': QualificationYear, 'University': University,
                 'Address': Address, 'AddQual1': AddQual1, 'AddQualYear1': AddQualYear1,
                 'AddQualUniv1': AddQualUniv1, 'AddQual2': AddQual2, 'AddQualYear2': AddQualYear2,
                 'AddQualUniv2': AddQualUniv2}, ignore_index=True)

            drivern.switch_to.window(drivern.window_handles[0])

        clk = 1
        try:
            while clk < 13:
                drivern.find_element_by_link_text('Next').click()
                time.sleep(10)
                clk += 1

        except (NoSuchElementException, TimeoutException):
            drivern.close()
            print "Reading done"
            exit(0)

def initial_setup(drivern):
    drivern.get("http://www.mciindia.org/InformationDesk/IndianMedicalRegister.aspx")
    drivern.find_element_by_link_text('State Medical Council').click()
    WebDriverWait(drivern, 10).until(EC.presence_of_element_located((By.ID, "dnn_ctr588_IMRIndex_Drp_StateCouncil")))
    Select(drivern.find_element_by_id("dnn_ctr588_IMRIndex_Drp_StateCouncil")).select_by_value(Medical_Council)


binary = FirefoxBinary( 'C:\Program Files (x86)\Mozilla Firefox\\firefox.exe' )

driver1 = webdriver.Firefox( firefox_binary=binary )
driver2 = webdriver.Firefox( firefox_binary=binary )
driver3 = webdriver.Firefox( firefox_binary=binary )
driver4 = webdriver.Firefox( firefox_binary=binary )
driver5 = webdriver.Firefox( firefox_binary=binary )
driver6 = webdriver.Firefox( firefox_binary=binary )
driver7 = webdriver.Firefox( firefox_binary=binary )
driver8 = webdriver.Firefox( firefox_binary=binary )
driver9 = webdriver.Firefox( firefox_binary=binary )
driver10 = webdriver.Firefox( firefox_binary=binary )
driver11 = webdriver.Firefox( firefox_binary=binary )
driver12 = webdriver.Firefox( firefox_binary=binary )

initial_setup(driver1)
initial_setup(driver2)
initial_setup(driver3)
initial_setup(driver4)
initial_setup(driver5)
initial_setup(driver6)
initial_setup(driver7)
initial_setup(driver8)
initial_setup(driver9)
initial_setup(driver10)
initial_setup(driver11)
initial_setup(driver12)

try:
    driver1.find_element_by_id( "dnn_ctr588_IMRIndex_Submit_Btn" ).click( )
    time.sleep( 10 )
    t1 = Thread( target=read, args=("driver1", driver1,) )
    t1.start()
except (NoSuchElementException):
    print "driver1 done"
    started1 = 0

try:
    driver2.find_element_by_id( "dnn_ctr588_IMRIndex_Submit_Btn" ).click( )
    time.sleep( 10 )
    driver2.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    t2 = Thread( target=read, args=("driver2", driver2,) )
    t2.start()
except (NoSuchElementException):
    print "driver2 done"
    started2 = 0

try:
    driver3.find_element_by_id( "dnn_ctr588_IMRIndex_Submit_Btn" ).click( )
    time.sleep( 10 )
    driver3.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver3.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    t3 = Thread( target=read, args=("driver3", driver3,) )
    t3.start()
except (NoSuchElementException):
    print "driver3 done"
    started3 = 0

try:
    driver4.find_element_by_id( "dnn_ctr588_IMRIndex_Submit_Btn" ).click( )
    time.sleep( 10 )
    driver4.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver4.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver4.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    t4 = Thread( target=read, args=("driver4", driver4,) )
    t4.start()
except (NoSuchElementException):
    print "driver4 done"
    started4 = 0

try:
    driver5.find_element_by_id( "dnn_ctr588_IMRIndex_Submit_Btn" ).click( )
    time.sleep( 10 )
    driver5.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver5.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver5.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver5.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    t5 = Thread( target=read, args=("driver5", driver5,) )
    t5.start()
except (NoSuchElementException):
    print "driver5 done"
    started5 = 0

try:
    driver6.find_element_by_id( "dnn_ctr588_IMRIndex_Submit_Btn" ).click( )
    time.sleep( 10 )
    driver6.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver6.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver6.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver6.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    driver6.find_element_by_link_text( 'Next' ).click( )
    time.sleep( 10 )
    t6 = Thread( target=read, args=("driver6", driver6,) )
    t6.start()
except (NoSuchElementException):
    print "driver6 done"
    started6 = 0

try:
    driver7.find_element_by_id("dnn_ctr588_IMRIndex_Submit_Btn").click()
    time.sleep(10)
    driver7.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver7.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver7.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver7.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver7.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver7.find_element_by_link_text('Next').click()
    time.sleep(10)
    t7 = Thread(target=read, args=("driver7", driver7,))
    t7.start()
except (NoSuchElementException):
    print "driver7 done"
    started7 = 0

try:
    driver8.find_element_by_id("dnn_ctr588_IMRIndex_Submit_Btn").click()
    time.sleep(10)
    driver8.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver8.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver8.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver8.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver8.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver8.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver8.find_element_by_link_text('Next').click()
    time.sleep(10)
    t8 = Thread(target=read, args=("driver8", driver8,))
    t8.start()
except (NoSuchElementException):
    print "driver8 done"
    started8 = 0

try:
    driver9.find_element_by_id("dnn_ctr588_IMRIndex_Submit_Btn").click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver9.find_element_by_link_text('Next').click()
    time.sleep(10)
    t9 = Thread(target=read, args=("driver9", driver9,))
    t9.start()
except (NoSuchElementException):
    print "driver9 done"
    started9 = 0

try:
    driver10.find_element_by_id("dnn_ctr588_IMRIndex_Submit_Btn").click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver10.find_element_by_link_text('Next').click()
    time.sleep(10)
    t10 = Thread(target=read, args=("driver10", driver10,))
    t10.start()
except (NoSuchElementException):
    print "driver10 done"
    started10 = 0

try:
    driver11.find_element_by_id("dnn_ctr588_IMRIndex_Submit_Btn").click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver11.find_element_by_link_text('Next').click()
    time.sleep(10)
    t11 = Thread(target=read, args=("driver11", driver11,))
    t11.start()
except (NoSuchElementException):
    print "driver11 done"
    started11 = 0

try:
    driver12.find_element_by_id("dnn_ctr588_IMRIndex_Submit_Btn").click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    driver12.find_element_by_link_text('Next').click()
    time.sleep(10)
    t12 = Thread(target=read, args=("driver12", driver12,))
    t12.start()
except (NoSuchElementException):
    print "driver12 done"
    started12 = 0



if started1 == 1:
    t1.join()

if started2 == 1:
    t2.join()

if started3 == 1:
    t3.join()

if started4 == 1:
    t4.join()

if started5 == 1:
    t5.join()

if started6 == 1:
    t6.join()

if started7 == 1:
    t7.join()

if started8 == 1:
    t8.join()

if started9 == 1:
    t9.join()

if started10 == 1:
    t10.join()

if started11 == 1:
    t11.join()

if started12 == 1:
    t12.join()

doc_list.to_excel('C:\\Dataset\\ASS.xlsx','Sheet1')
