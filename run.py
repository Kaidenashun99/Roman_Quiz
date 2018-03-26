import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    """Landing Page for users"""
    return render_template("index.html", page_title="Home page")
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)
  