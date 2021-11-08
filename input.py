from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

fo = open('input_text.txt' 'w')
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#### Code to run webside

driver.get("https://thescheduler.pythonanywhere.com/course_select%22")

department = driver.find_element_by_id("fdept")
crs = department

course_number = driver.find_element_by_id("fcrs")
crn = course_number

driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/registration/registration%22")

schedule = driver.find_element_by_id('catalogSearchLink')
schedule.click

select = driver.find_element_by_id("select2-drop-mask")
select.send_keys("2022 spring")

term = driver.find_element_by_id("term-go")
term.click

subject = driver.find_element_by_id("select2-container")
subject.send_keys(crs)

crnum = driver.find_element_by_name("txt_course_number_range_From")
crnum.send_keys(crn)

search = driver.find_element_by_id("search-go")
search.click

time.sleep(10) # waits 5 seconds

print(crs, crn, file = fo )
driver.quit()
fo.close()



