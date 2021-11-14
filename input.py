from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import time

#fo = open('input_text.txt' 'w')
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

#### Code to run webside

driver.get("https://thescheduler.pythonanywhere.com/course_select")

##time.sleep(5)
department = driver.find_element_by_id("fdept")
crs = department

course_number = driver.find_element_by_id("fcrs")
crn = course_number

driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
#driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch")

time.sleep(5)

sel = driver.find_element_by_id('s2id_txt_term')
sel.click()

#sel.select_by_visible_text("Spring 2022")
time.sleep(2)

select = driver.find_element_by_id("s2id_autogen1_search")
select.send_keys('2022 Spring')
time.sleep(1)
select.click()
#select.select_by_value('2022 Spring')

time.sleep(1)
spring = driver.find_element_by_id("select2-results-1")
spring.click()
#spring.select_by_visible_text('2022 Spring')

submit = driver.find_element_by_id('term-go')
submit.click()

## "select2-result-label-23"
subject = driver.find_element_by_id("select2-container")
subject.send_keys(crs)

crnum = driver.find_element_by_name("txt_course_number_range_From")
crnum.send_keys(crn)

search = driver.find_element_by_ID("search-go")
search.click

CourseTitle = driver.find_element_by_ID("650874")
print(CourseTitle)


time.sleep(10) # waits 5 seconds

#print(crs, crn, file = fo )
driver.quit()
#fo.close()



