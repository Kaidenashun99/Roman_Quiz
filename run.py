import os
from flask import Flask, redirect, render_template, request, flash
import json
from quiz import get_question

app = Flask(__name__)
app.secret_key = 'some secret'



""" Writes data to selected file """ 
def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)


@app.route('/', methods=["GET", "POST"])
def index():
    """Home Page for users"""
    if request.method == "POST":
            flash("Thanks, you selected {} as your username".format(request.form["username"]))
    return render_template("index.html", page_title="Home page")
    

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    return render_template("quiz.html", page_title="Quiz")
    
    
   
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)
  