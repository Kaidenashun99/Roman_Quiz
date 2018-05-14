import os
from flask import Flask, redirect, render_template, request, flash, session
import json


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
        session['username'] = request.form['username']
        return redirect("/quiz")
    return render_template("index.html", page_title="Home page")
    

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    
    username = session['username']

    with open('data/questions.json') as json_data:
        data = json.load(json_data)
        
    if request.method=="POST":
        return redirect("/results")
    return render_template("quiz_ckz.html", page_title="Quiz", quiz_data=data, username=username)

@app.route('/results', methods=["GET", "POST"]) 
def results():
    score = 0
    
    with open("data/answers.json") as answers:
        answers_dict = json.load(answers)
        for key in list(answers_dict.keys()):
            question_id = int(answers_dict[key]['id'])
            answer = answers_dict[key]['answer']
            
            i = 1
            while i < 11:
                print(request.form.get('question' + str(i)))
                print(answer)
                if question_id == i and request.form.get('question' + str(i)) == answer:
                    score =+1 
                i+=1
                
    session['score'] = score
    print('score: ', score)
    # raise SystemExit
    
    return render_template("results.html", page_title="Leaderboard")
    
def leaderboard():
    username = session['username']
    
    score = session['score']
    
    write_to_file(username +" "+ score, "data/leaderboard.json")
        
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)
  