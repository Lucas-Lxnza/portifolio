from main import app
from flask import render_template

#routes
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/RDX")
def rdx():
  return "C4"