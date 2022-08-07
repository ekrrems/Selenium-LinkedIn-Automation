# Linkedin Messaging Automation

import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
import numpy as np

# *************#
our_username = 'ekremserdarozturk@hotmail.com'
our_password = 'adanali_01'
# *************#
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

# *************#
service_obj = Service(r'C:\Users\Hp\Desktop\hp yedekler\masaustu\Global AI Hub\Selenium\chromedriver1.exe')
driver = webdriver.Chrome(service=service_obj)
# *************#
driver.get(url)

# Loading Excel Sheet
excel_sheet = pd.read_excel(r'C:\Users\Hp\Desktop\hp yedekler\masaustu\Global AI Hub\Selenium\Community Database .xlsx')
# print(excel_sheet[4:10].columns)
# print(excel_sheet[['Name','LinkedIn Profile Link']][4:10])





def log_in(username, password):
    """Log into your LinkedIn Page"""
    username = driver.find_element(by=By.XPATH, value="//input[@name ='session_key']")
    password = driver.find_element(by=By.XPATH, value="//input[@name ='session_password']")

    time.sleep(1)
    username.send_keys(our_username)
    time.sleep(1)
    password.send_keys(our_password)

    time.sleep(2)
    submit = driver.find_element(by=By.XPATH, value= "//button[@type = 'submit']")
    submit.click()


# To open LinkedIn Page


log_in(our_username, our_password)


def new_contact(contact_url):
    """Opens the page of contact"""
    driver.get(contact_url)
    time.sleep(2)


def press_connect():
    """Presses the connetc button if the button is on the page"""
    # Press Connect Button
    buttons = driver.find_elements(by=By.TAG_NAME,value='button')
    baglanti_button = [btn for btn in buttons if btn.text == 'Bağlantı kur']
    baglanti_button[0].click()
    time.sleep(2)


def add_note(name):
    """Adds note after connect is clicked"""
    note = driver.find_element(by=By.XPATH,value="//button[@aria-label = 'Not ekle']")
    note.click()

    script = f"""Hi {name}, I hope you are doing well. I am Ekrem, reaching out to you from Global AI Hub, AI Team. We would like to invite you to an amazing mentorship opportunity in our huge bootcamps that we organize all around the world. To talk further, please accept my invitation."""
    # Add script
    textarea = driver.find_element(by=By.XPATH,value="//textarea[@id = 'custom-message']")
    textarea.click()
    textarea.send_keys(script)
    time.sleep(3)

    # Press Send Button
    send_button = driver.find_element(by=By.XPATH,value="//button[@aria-label ='Şimdi gönder']")
    send_button.click()
    time.sleep(3)


def connect_in_more():
    """Clicks connect that is in the 'Daha Fazla'"""
    more = driver.find_element(by=By.XPATH,value="//button[@aria-label = 'Daha fazla işlem']")
    driver.execute_script("arguments[0].click();", more)
    time.sleep(2)
    connect = driver.find_element(by=By.XPATH,value="//li-icon[@type = 'connect']")
    connect.click()


for i, j in excel_sheet[['Name', 'LinkedIn Profile Link']][20:30].values:
    name = (str(i).split())[0]
    contact_url = str(j)

    try:
        new_contact(contact_url=contact_url)
        press_connect()
        add_note(name=name)
        print(i)

    except selenium.common.exceptions.ElementClickInterceptedException:
        connect_in_more()
        add_note(name=name)
        print(i)
    finally:
        continue
