from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    kanjiData = {"translation":"1","kanji":"一","pronunciation":"ICHI, ITSU"}
    return render_template("index.html", kanjiData=kanjiData)

@app.route("/about")
def about():
    return render_template("about.html")