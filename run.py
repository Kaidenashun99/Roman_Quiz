import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

""" Writes data to selected file """ 
def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)


@app.route('/', methods=["GET", "POST"])
def index():
    """Landing Page for users"""""
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
                user_list.write(request.form["username"] + "\n")
                return redirect("quiz")
    return render_template("index.html", page_title="Home page")
    


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)
  