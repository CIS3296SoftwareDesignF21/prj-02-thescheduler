# Felix Rabinovich
# TheScheduler

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


print("Welcome to the scheduler, the program that automates the process of signing up for classes.")
print('please enter TU portal login ')
usr = input('Username:')
pas = input('Password:')


#### Code to run webside

driver.get('https://tuportal5.temple.edu/')
print(driver.title)

usrname = driver.find_element_by_id("username")
usrname.send_keys(usr)

pssword = driver.find_element_by_id("password")
pssword.send_keys(pas)

login = driver.find_element_by_name('_eventId_proceed')
login.click()

stuLink = driver.find_element_by_link_text('Student Tools')
stuLink.click()

regClass = driver.find_element_by_link_text('Plan Your Schedule')
regClass.click()

term = driver.find_element_by_id('select2-drop-mask')
term.click()
termGo = driver.find_element_by_link_text('2022 Spring')
termGo.click()

time.sleep(5) # waits 5 seconds
driver.quit()


#### twillo

#### web scraping (Beautiful Soup)
