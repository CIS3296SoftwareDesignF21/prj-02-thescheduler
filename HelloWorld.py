from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is the main page of the soon to be SCHEDULER !!" \
           "<h1>Hello World<h1>" \
           "<p>Hello this is Felix" \
           "<br>Hello this is Abin" \
           "<br>Hello this is Ethan" \
           "<br>Hello this is ____" \
           "<br>Hello this is ____" \
           "<br>Hello this is ____<p>"

if __name__ == "__main__":
    app.run()