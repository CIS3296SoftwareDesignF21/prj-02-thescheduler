from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import deque
import time


# fo = open('input_text.txt' 'w')
# PATH = "/usr/local/bin/chromedriver" # For MAC
PATH = "C:\Program Files (x86)\chromedriver.exe"  # For Windows
driver = webdriver.Chrome(PATH)

#### Code to run webside

driver.get("https://thescheduler.pythonanywhere.com/course_select")

department = driver.find_element_by_id("fdept")
crs = department

course_number = driver.find_element_by_id("fcrs")
crn = course_number

driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
# driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch")


select = driver.find_element_by_class_name("select2-drop")
select.send_keys("2022 Spring")

term = driver.find_element_by_id("term-go")
term.click

subject = driver.find_element_by_id("select2-container")
subject.send_keys(crs)

crnum = driver.find_element_by_name("txt_course_number_range_From")
crnum.send_keys(crn)

search = driver.find_element_by_id("search-go")
search.click

CourseTitle = driver.find_element_by_id("650874")
print(CourseTitle)

time.sleep(10)  # waits 5 seconds

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
