from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import time

#PATH = "/usr/local/bin/chromedriver"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#### Code to run webside

driver.get("https://thescheduler.pythonanywhere.com/course_select")

time.sleep(2)
department = driver.find_element_by_id("fdept")
crs = department

course_number = driver.find_element_by_id("fcrs")
crn = course_number

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
## works till here


'''
time.sleep(2)
crnum = driver.find_element_by_name("txt_courseNumber")
crnum.send_keys('3207')
'''

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


'''
search_again = driver.find_element_by_id("search-again-button")
search_again.click()   Needed for loop 

CourseTitle = driver.find_element_by_id("courseTitle")
print(CourseTitle)    This print is to check if the scrapper is working

section_number = driver.find_element_by_id("sectionNumber")
print(section_number)

credit_hours = driver.find_elements_by_name("Credit Hours:")
print(credit_hours)

'''


time.sleep(10) # waits 5 seconds

# Dictionary storing for course info
Schedule = {1: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''},
            2: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''},
            3: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''},
            4: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''}}
"""
classQueue is a queue implemented using deque() who's elements consist of courses.
Classes are dict entries structured the following way: 

{'Subject': '', 'Course Number': ''}

Example: {'Subject': 'Computer & Information Science', 'Course Number': '3296'}

"""
###
""" !! Browse Courses page must be navigated to prior to loop !!

select = driver.find_element_by_class_name("select2-drop")
select.send_keys("2022 Spring")

term = driver.find_element_by_id("term-go")
term.click
"""
def parseQueue(courseQueue):
    while courseQueue:
        currentClass = courseQueue.pop() #Store the next entry in memory, delete it from the queue
        currentSubject = currentClass['Subject']
        currentCourseNum = currentClass['Course Number']



        subject = driver.find_element_by_id("select2-container")
        subject.send_keys(currentSubject)

        crnum = driver.find_element_by_name("txt_course_number_range_From")
        crnum.send_keys(currentCourseNum)

        search = driver.find_element_by_id("search-go")
        search.click

        # Experimental from here till end of loop
        crsSelect = driver.find_element_by_class_name("form-button search-section-button")
        crsSelect.click

        #callCourseScraper

        backToSearch = driver.find_element_by_class_name("form-button return-course-button")
        backToSearch.click

        searchAgain = driver.find_element_by_id("search-again-button")
        searchAgain.click


    return
# print(crs, crn, file = fo )
driver.quit()
# fo.close()

