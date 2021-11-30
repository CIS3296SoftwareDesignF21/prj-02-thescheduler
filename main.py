from flask import Flask, redirect, url_for, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from twilio.rest import Client
import time
import requests
import lxml.html as lh
app = Flask(__name__)

"""
Used the following as a guide:
https://www.techwithtim.net/tutorials/flask/http-methods-get-post/
"""

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/course_select", methods=["POST", "GET"])
def course_select():
    all_courses = {"course1": {}, "course2": {}, "course3": {}, "course4": {}}
    if request.method == "POST":
        dept = request.form["fdept"]
        crs1 = request.form["fcrs1"]
        crs2 = request.form["fcrs2"]
        crs3 = request.form["fcrs3"]
        crs4 = request.form["fcrs4"]

        return redirect(
            url_for("get_course", department=dept, course_number1=crs1))
    else:
        return render_template("index.html")


@app.route("/<department>&<course_number1>")
def get_course(department, course_number1):
    file = open("scraped_details.txt", "w")
    PATH = "/usr/local/bin/chromedriver"
    #PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    # page = requests.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
    driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
    # driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch")

    sel = driver.find_element_by_id('s2id_txt_term')
    sel.click()

    # sel.select_by_visible_text("Spring 2022")
    time.sleep(2)

    select = driver.find_element_by_id("s2id_autogen1_search")
    select.send_keys('2022 Spring')
    time.sleep(1)
    select.click()
    # select.select_by_value('2022 Spring')

    time.sleep(1)
    spring = driver.find_element_by_id("select2-results-1")
    spring.click()
    # spring.select_by_visible_text('2022 Spring')

    submit = driver.find_element_by_id('term-go')
    submit.click()

    time.sleep(1)

    subject_before = driver.find_element_by_id("s2id_txt_subject")
    subject_before.click()

    subject_after = driver.find_element_by_id("s2id_autogen1")
    subject_after.send_keys(department)
    time.sleep(1)
    subject_after.send_keys(Keys.RETURN)

    crnum_from = driver.find_element_by_name("txt_course_number_range_From")
    crnum_from.click()
    crnum_from.send_keys(course_number1)

    crnum_to = driver.find_element_by_name("txt_course_number_range_To")
    crnum_to.send_keys(course_number1)

    search = driver.find_element_by_id("search-go")
    search.click()

    time.sleep(1)
    view_sections = driver.find_element_by_class_name("form-button.search-section-button")
    view_sections.click()

    time.sleep(1)
    table = driver.find_element(By.ID, "table1")
    table_body = table.find_element(By.TAG_NAME, "tbody")
    rows = table_body.find_elements(By.TAG_NAME, "tr")

    course_results = {"credits": "0", "sections": []}
    all_sections = []

    # "//tagname[@Atrribute='Value']"
    for row in rows:
        crn = row.find_element(By.XPATH, "//td[@data-property='courseReferenceNumber']")
        course_results["credits"] = row.find_element(By.XPATH, "//td[@data-property='creditHours']").text

        meeting_times = []
        prof_td = row.find_element(By.XPATH, "//td[@data-property='instructor']")
        prof = prof_td.find_element(By.CLASS_NAME, "email").text # Professor's name
        print("Prof = ", prof)

        meeting_td = row.find_element(By.XPATH, "//td[@data-property='meetingTime']")
        meetings = row.find_elements(By.CLASS_NAME, "meeting")
        for meeting in meetings:
            meeting_map = {"day": "", "start": "", "end": "", "instructor": prof}

            day = meeting.find_element(By.XPATH, "//div[@class='ui-pillbox-summary screen-reader']").text
            meeting_map["day"] = day

            time_range = meeting.find_element(By.TAG_NAME, "span") # time range is nested spans
            i = 0
            start, end = "", ""
            for span in time_range.find_elements(By.TAG_NAME, "span"): #loops 4 times
                if i == 0:
                    start += span.text
                    start += ":"
                    i += 1
                    continue
                if i == 1:
                    start += span.text
                    i += 1
                    continue
                if i == 2:
                    end += span.text
                    end += ":"
                    i += 1
                if i == 3:
                    end += span.text
                    i += 1
            meeting_map["start"] = start
            meeting_map["end"] = end
            meeting_times.append(meeting_map)
        section = (crn, meeting_times)
        all_sections.append(section)
    file.close()
    driver.quit()
    course_results["sections"] = all_sections
    print(course_results)
    return course_results
    #######################################################################
    """
    
    time.sleep(1)

    before_course_number = driver.find_element_by_class_name("odd")
    before_course_number.click()

    time.sleep(3)
    course_number = driver.find_elements_by_class_name('odd')
    # digit = course_number.text
    for element in course_number:
        # print (course_number.text)
        # print(driver.find_element_by_class_name("readonly.add-row-selected").text)
        print(element.text, file=file)

    time.sleep(2)
    course_number = driver.find_elements_by_class_name('even')
    # digit = course_number.text
    for element in course_number:
        # print (course_number.text)
        # print(driver.find_element_by_class_name("readonly.add-row-selected").text)
        print(element.text, file=file)

    time.sleep(10)  # waits 10 seconds
    file.close()

    driver.quit()
    """

    ''' THIS IS ERIKS QUE CODE
    # Dictionary storing for course info
    Schedule = {1: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''},
                2: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''},
                3: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''},
                4: {'Title': '', 'Time': '', 'Instructor': '', 'Credits': ''}}

    classQueue is a queue implemented using deque() who's elements consist of courses.
    Classes are dict entries structured the following way: 

    {'Subject': '', 'Course Number': ''}

    Example: {'Subject': 'Computer & Information Science', 'Course Number': '3296'}


    ###
    !! Browse Courses page must be navigated to prior to loop !!

    select = driver.find_element_by_class_name("select2-drop")
    select.send_keys("2022 Spring")

    term = driver.find_element_by_id("term-go")
    term.click

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
    '''

def twilio():
    TWILIO_SID = 'ACbf02fe253cef5d92aac22aa3bd5b1676'
    TWILIO_TOKEN = ''
    TWILIO_PHONE = '+12156087254'

    client = Client(TWILIO_SID, TWILIO_TOKEN)

    def sendOneMessage(sendTo):
        client.messages.create(body="Hey There ! Your schedule is complete, you can take a look at it on our site !",
                               from_=TWILIO_PHONE, to=sendTo)

    sendOneMessage('+12158079223')

    print('SMS sent succesfully')

if __name__ == "__main__":
    app.run(debug=True)
