from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import sys
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
PATH = os.path.join(sys.path[0], "chromedriver")

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')



print("Welcome to the scheduler, the program that automates the process of signing up for classes.")
print('please enter TU portal login ')
usr = input('Username:')
pas = input('Password:')

browser = webdriver.Chrome(PATH, options = chrome_options)
browser.get("https://tuportal5.temple.edu/")

usrname = browser.find_element_by_id("username")
usrname.send_keys(usr)

pssword = browser.find_element_by_id("password")
pssword.send_keys(pas)

login = browser.find_element_by_name('_eventId_proceed')
login.click()
time.sleep(1)

stuLink = browser.find_element_by_link_text('Student Tools')
stuLink.click()

regClass = browser.find_element_by_link_text('Plan Your Schedule')
regClass.click()

browser.save_screenshot("HeadlessTestingScreenshot.png")

browser.quit()