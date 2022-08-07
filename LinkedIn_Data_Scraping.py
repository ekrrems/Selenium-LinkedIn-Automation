# Creating a Database
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
# driver = webdriver.Chrome(r'C:\Users\Hp\Desktop\hp yedekler\masaustu\Global AI Hub\Selenium\chromedriver1.exe')
driver = webdriver.Chrome(service=service_obj)
# *************#
driver.get(url)


def log_in(username, password):
    """Log into your LinkedIn Page"""
    username = driver.find_element(by=By.XPATH, value="//input[@name ='session_key']")
    password = driver.find_element(by=By.XPATH, value="//input[@name ='session_password']")

    time.sleep(1)
    username.send_keys(our_username)
    time.sleep(1)
    password.send_keys(our_password)

    time.sleep(2)
    submit = driver.find_element(by=By.XPATH, value="//button[@type = 'submit']")
    submit.click()


log_in(our_username, our_password)


def searching(search):
    search_button = driver.find_element(by=By.XPATH,
                                        value="//input[@class = 'search-global-typeahead__input always-show-placeholder']")
    search_button.click()
    time.sleep(1)
    search_button.send_keys(search)
    time.sleep(2)
    search_button.send_keys(Keys.RETURN)
    time.sleep(6)

    buttons = driver.find_elements(by=By.TAG_NAME, value="button")
    time.sleep(2)
    people_button = [btn for btn in buttons if btn.text == 'Kişiler']
    people_button[0].click()


def country_Selection(country):
    country_Button = driver.find_element(by=By.XPATH,
                                         value="//button[@aria-label = 'Konumlar filtre. Bu düğmeyi tıklamak tüm Konumlar filtreyi gösterir.']")
    country_Button.click()
    time.sleep(2)
    search_Bar = driver.find_element(by=By.XPATH, value="//input[@placeholder = 'Konum ekle']")
    search_Bar.click()
    time.sleep(1)
    search_Bar.send_keys(country)
    time.sleep(1)
    search_Bar.send_keys(Keys.DOWN)
    time.sleep(1)
    search_Bar.send_keys(Keys.RETURN)
    time.sleep(3)
    result_button = driver.find_element(by=By.XPATH,
                                        value="/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]")
    result_button.click()
    time.sleep(4)


def next_Page():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    next_button = driver.find_element(by=By.XPATH,
                                      value="//li-icon[@type ='chevron-right-icon']")
    next_button.click()
    time.sleep(6)


search = 'Data analyst'
country = 'Hindistan'
searching(search=search)
time.sleep(7)
country_Selection(country=country)
time.sleep(4)
# #Data Scraping
# lists
name_list = []
role_list = []
urls = []
company_list = []

try:
    for p in range(3):
        # Names
        names = driver.find_elements(by=By.XPATH, value="//span[@dir='ltr']")
        for i in range(len(names)):
            name_list.append(names[i].text.split('\n')[0])

        # roles

        roles = driver.find_elements(by=By.XPATH,
                                     value="//div[@class ='entity-result__primary-subtitle t-14 t-black t-normal']")

        for i in range(len(roles)):
            if roles[i] != None:
                role_list.append(roles[i].text)
            else:
                role_list.append('None')

        # Linkedin Urls

        linkedin_urls = driver.find_elements(by=By.XPATH,
                                             value="//span[@class = 'entity-result__title-text t-16']/a")

        for i in range(len(linkedin_urls)):
            if linkedin_urls[i] != None:
                urls.append(linkedin_urls[i].get_attribute('href'))
            else:
                urls.append('None')

        # Company

        companies = driver.find_elements(by=By.XPATH,
                                         value="//p[starts-with(@class,'entity-result__summary')]")

        for i in range(len(companies)):
            if companies[i] != None:
                company_list.append(companies[i].text.split(' ')[2])
            else:
                company_list.append('None')

        next_Page()
        time.sleep(2)

except selenium.common.exceptions.NoSuchElementException:
    print(name_list)
    print(role_list)
    print(urls)
    print(company_list)

print(name_list)
print(role_list)
print(urls)
print(company_list)

create_DB = str(input("To create database press: 'd',to continue press: 'c'"))

if create_DB == 'd':
    data = pd.DataFrame({'Name': name_list, 'Role': role_list,
                         'Company': company_list, 'LinkedIn': urls, 'Country': [country for c in range(len(urls))]})
    writer = pd.ExcelWriter(f'C:\\Users\\Hp\\Desktop\\Automation_Outputs\\{search}_in_{country}.xlsx')
    data.to_excel(writer)
    writer.save()
elif create_DB == 'c':
    pass
