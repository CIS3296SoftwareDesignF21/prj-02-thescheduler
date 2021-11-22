from flask import Flask, redirect, url_for, render_template, request, session
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

app = Flask(__name__)
'''
global department
global course1
global course2
global course3
global course4
'''
"""
Used the following as a guide:
https://www.techwithtim.net/tutorials/flask/http-methods-get-post/
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/course_select", methods=["POST", "GET"])
def course_select():
    if request.method == "POST":
        dept = request.form["fdept"]
        crs1 = request.form["fcrs1"]
        crs2 = request.form["fcrs2"]
        crs3 = request.form["fcrs3"]
        crs4 = request.form["fcrs4"]
        print(dept, crs1, crs2, crs3, crs4)

        department = dept
        course1 = crs1
        course2 = crs2
        course3 = crs3
        course4 = crs4

        post_course(dept, crs1)

        return redirect(
            url_for("post_course", department=dept, course_number1=crs1, course_number2=crs2, course_number3=crs3,
                    course_number4=crs4)
        )
    else:
        return render_template("index.html")


app.route("/<department> & <course_number1> & <course_number2>")
def post_course(department, course_number1, course_number2):
    PATH = "/usr/local/bin/chromedriver"
    i = 0
    while (i < 2):
        if (i == 1):

            # PATH = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)

            driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
        #   driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch")

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

            time.sleep(10)  # waits 5 seconds

        if(i == 1):
            # PATH = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)

            driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch")
            #   driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch")

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
            crnum_from.send_keys(course_number2)

            crnum_to = driver.find_element_by_name("txt_course_number_range_To")
            crnum_to.send_keys(course_number2)

            search = driver.find_element_by_id("search-go")
            search.click()

            time.sleep(1)
            view_sections = driver.find_element_by_class_name("form-button.search-section-button")
            view_sections.click()

            time.sleep(10)  # waits 5 seconds
    i += 1


# driver.quit()


if __name__ == "__main__":
    app.run(debug=True)
