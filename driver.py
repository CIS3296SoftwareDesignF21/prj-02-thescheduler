from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

"""
Used the following as a guide:
https://www.techwithtim.net/tutorials/flask/http-methods-get-post/
"""


# import main

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
        # main() #integrated but has bugs
        return redirect(
            url_for("post_course", department=dept, course_number1=crs1, course_number2=crs2, course_number3=crs3,
                    course_number4=crs4))
    else:
        return render_template("index.html")


@app.route("/<department>&<course_number1>&<course_number2>&<course_number3>&<course_number4>")
def post_course(department, course_number1, course_number2, course_number3, course_number4):
    return f"<h1>Go CST!! You're taking:{department},{course_number1}</h1>" \
           f"<h1>Go CST!! You're taking:{department},{course_number2}</h1>" \
           f"<h1>Go CST!! You're taking:{department},{course_number3}</h1>" \
           f"<h1>Go CST!! You're taking:{department},{course_number4}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
