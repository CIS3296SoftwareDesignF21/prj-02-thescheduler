from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

PATH = "/usr/local/bin/chromedriver"
#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
#driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch")


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


time.sleep(1)

subject_before = driver.find_element_by_id("s2id_txt_subject")
subject_before.click()


subject_after = driver.find_element_by_id("s2id_autogen1")
subject_after.send_keys('CIS')
time.sleep(1)
subject_after.send_keys(Keys.RETURN)


crnum_from = driver.find_element_by_name("txt_course_number_range_From")
crnum_from.click()
crnum_from.send_keys('3207')


crnum_to = driver.find_element_by_name("txt_course_number_range_To")
crnum_to.send_keys('3207')


search = driver.find_element_by_id("search-go")
search.click()

time.sleep(1)
view_sections = driver.find_element_by_class_name("form-button.search-section-button")
view_sections.click()

#######################################################################
time.sleep(1)

before_course_number = driver.find_element_by_class_name("odd")
before_course_number.click()

time.sleep(3)
course_number = driver.find_elements_by_class_name('odd')
#digit = course_number.text
for element in course_number:
    #print (course_number.text)
    #print(driver.find_element_by_class_name("readonly.add-row-selected").text)
    print(element.text)




time.sleep(10) # waits 10 seconds

driver.quit()
