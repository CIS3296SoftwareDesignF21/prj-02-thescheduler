from flask import Flask, redirect, url_for, render_template, request

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
    if request.method == "POST":
        dept = request.form["fdept"]
        crs = request.form["fcrs"]
        return redirect(url_for("post_course", department=dept, course_number=crs))
    else:
        return render_template("index.html")

@app.route("/post_course")
def post_course(department, course_number):
        return f"<h1>Go CST!! You're taking:{department},{course_number}</h1>"

if __name__ == "__main__":
    app.run(debug=True)