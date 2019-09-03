from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


# Adding a new route, like a subdirectory
@app.route("/stowers")
def stowers():
    return "Hello, Robert.  Welcome back!"


if __name__ == "__main__":
    app.run(debug=True)