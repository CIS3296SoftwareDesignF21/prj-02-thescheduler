from flask import Flask, redirect, url_for, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
import time
import requests
import lxml.html as lh
app = Flask(__name__)

"""
Used the following as a guide:
https://www.techwithtim.net/tutorials/flask/http-methods-get-post/
"""

"""
Created By: 
    Felix Rabinovich, 
    Ethan Lewis, 
    Abin Cheryian, 
    Erik Adrian Rodriguez,
    Dylan Dunda,
    Ryan Joseph Babala
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

        courses = crs1+','+crs2+','+crs3+','+crs4

        return redirect(
            url_for("get_course", department=dept, courses_input=courses))
    else:
        return render_template("index.html")


@app.route("/<department>&<courses_input>")
def get_course(department, courses_input):
    course_list = courses_input.split(',')
    print("course list = ", course_list)
    all_sections = {}
    print("all sections = ", all_sections)
    all_courses = {}
    crn = 0
    for idx, course_number in enumerate(course_list):
        course_results = {"credits": "0", "sections": {}}
        print()
        print()
        print("Course number = ", course_number)
        if course_number is None or course_number.isdigit() != True:
            print("No course given")
        else:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
            PATH = "/usr/local/bin/chromedriver"
            #PATH = "C:\Program Files (x86)\chromedriver.exe"

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

            driver = webdriver.Chrome(PATH, options = chrome_options)
            #driver = webdriver.Chrome(PATH)


            # page = requests.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
            driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
            # driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch")
            time.sleep(3)
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
            crnum_from.send_keys(course_number)

            crnum_to = driver.find_element_by_name("txt_course_number_range_To")
            crnum_to.send_keys(course_number)

            search = driver.find_element_by_id("search-go")
            search.click()

            time.sleep(1)
            view_sections = driver.find_element_by_class_name("form-button.search-section-button")
            view_sections.click()

            time.sleep(2)
            table = driver.find_element(By.ID, "table1")
            table_body = table.find_element(By.TAG_NAME, "tbody")
            rows = table_body.find_elements(By.TAG_NAME, "tr")

            section_results = {}

            # "//tagname[@Atrribute='Value']"
            for row in rows: #sections of a course
                print("-------")
                course_results["credits"] = row.find_element(By.XPATH, "//td[@data-property='creditHours']").text

                #crn = row.find_element(By.XPATH, "//td[@data-property='courseReferenceNumber']").get_attribute('innerHTML')
                #print("crn = ", crn)
                crn += 1
                meeting_times = []

                prof_td = row.find_element(By.XPATH, "//td[@data-property='instructor']")
                prof = prof_td.find_element(By.CLASS_NAME, "email").get_attribute('innerHTML') # Professor's name
                print("Prof = ", prof)

                meeting_td = row.find_element(By.XPATH, "//td[@data-property='meetingTime']")
                meetings = row.find_elements(By.CLASS_NAME, "meeting")
                for meeting in meetings:
                    dayParent = meeting.find_element(By.CLASS_NAME, "ui-pillbox")
                    day = dayParent.find_element(By.CLASS_NAME, "ui-pillbox-summary").get_attribute('innerHTML')
                    #day = meeting.find_element(By.XPATH, "//*[contains(@title,'Class on')]//descendant::div[1]").get_attribute('innerHTML')
                    #day = dayPrelim.find_element(By.XPATH, "//div[@class='ui-pillbox-summary screen-reader']").text
                    print("Day = ", day)

                    time_range = meeting.find_element(By.TAG_NAME, "span") # time range is nested spans
                    i = 0
                    start, end = "", ""
                    print(time_range.text)
                    for span in time_range.find_elements(By.TAG_NAME, "span"): #loops 4 times
                        #print("current span = ", span.get_attribute('innerHTML'))
                        #print("i = ", i)
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
                            continue

                        if i == 3:
                            end += span.get_attribute('innerHTML')
                            i += 1
                            continue

                    if ',' in day: # Multiple days per 1 meeting time of day
                        days_split = day.split(",")
                        for meeting_day in days_split:
                            meeting_map = {"day": meeting_day, "start": start, "end": end, "instructor": prof}
                            meeting_times.append(meeting_map)
                    else:
                        meeting_map = {"day": day, "start": start, "end": end, "instructor": prof}
                        meeting_times.append(meeting_map)

                section_results[crn] = meeting_times
                print("section results = ", section_results)
            course_results["sections"] = section_results
            driver.quit()
            all_courses[course_number] = course_results
            print("** All courses: ", all_courses)
    return render_template("output.html", final_results = all_courses)


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
