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


# *************#
our_username = str(input('Your E-mail Adress'))
our_password = str(input('Your Password'))

# *************#
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

# *************#
service_obj = Service(r'chromedriver1.exe')
driver = webdriver.Chrome(service=service_obj)
# *************#
driver.get(url)

# Loading Excel Sheet
excel_sheet = pd.read_excel(r'Excel_file')
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

    script = f"""Message To Send"""
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
    more = driver.find_element(by=By.XPATH,value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/button")
    time.sleep(1)
    more.click()
    time.sleep(2)
    connect = driver.find_element(by=By.XPATH,value="/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/div/div/ul/li[4]/div/li-icon")
    connect.click()

def direct_message():
    message_button = driver.find_element(by=By.XPATH, value= "//section[@class = 'artdeco-card ember-view pv-top-card']/div[2]/div[3]/div/div[2]/button")
    message_button.click()
    time.sleep(2)

    connect_button = driver.find_element(by=By.XPATH , value="//section[@class = 'artdeco-card ember-view pv-top-card']/div[2]/div[3]/div/div[2]/div/div/ul/li[5]/div/li-icon")
    time.sleep(1)
    connect_button.click()

def work_related():
    button = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/button[3]")
    time.sleep(1)
    button.click()
    time.sleep(1)

    connect =driver.find_element(by=By.XPATH, value= "/html/body/div[3]/div/div/div[3]/button")
    connect.click()






for i, j in excel_sheet[['Name', 'LinkedIn']][348:355].values:
    name = (str(i).split())[0]
    contact_url = str(j)
    time.sleep(2)

    new_contact(contact_url=contact_url)
    parent_div = driver.find_element(by=By.XPATH,
                                     value="//section[@class = 'artdeco-card ember-view pv-top-card']/div[2]/div[3]/div")
    divs = parent_div.find_elements(by=By.XPATH, value="./*")
    div_names = []
    for a in divs:
        div_names.append(a.text)

    num_of_divs = len(parent_div.find_elements(by=By.XPATH, value="./*"))
    try:
        if num_of_divs == 2:

            try:
                time.sleep(2)
                direct_message()
                add_note(name=name)
                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                work_related()
                time.sleep(3)
                add_note(name=name)
                print(i)
            finally:
                continue
        elif num_of_divs >= 3:
            time.sleep(0)
            if div_names[0] == 'Bağlantı kur':
                press_connect()
                add_note(name=name)
                print(i)

            elif div_names[0] == 'Takip Et':
                connect_in_more()
                add_note(name=name)
                print(i)
    finally:
        continue
