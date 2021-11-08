from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/") ## we dont have an url for the website yet so ...

input = open('input.txt', 'w')
time.sleep(10)

course_dept = driver.find_element_by_id("fdept")
search = driver.find_element_by_name("fcrs")

print(search, course_dept, file = input)


input.close()



