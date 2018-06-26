import os
from flask import Flask, redirect, render_template, request, flash, session
import json


app = Flask(__name__)
app.secret_key = 'some secret'

"""Functions"""
#Get the question data 
def get_question(index):
    with open('data/questions.json') as question_data:
        question = json.loads(question_data.read())
        return question[index] if index < 9 else None

def initialize_game(username):
    score = 0
    attempt = 1
    question = get_question(0)
    context = {
        'question_index' : 0,
        'question' : question['question_text'],
        'answer' : question['question_answer'],
        'decoy_answer_1' : question['decoy_answer_1'],
        'decoy_answer_2' : question['decoy_answer_2'],
        'decoy_answer_3' : question['decoy_answer_3'],
        'username' : username,
        'current_score' : score,
        'attempt' : attempt,
        }
    return context

def get_leaderboard():
    with open('data/leaderboard.txt', 'r') as leaderboard_file:
        list_of_leaders = leaderboard_file.readlines()
        userscores = []
        for leader in list_of_leaders:
            split_leaders = leader.split(':')
            username = split_leaders[0]
            score = split_leaders[1]
            user_score_combo = (username, score)
            userscores.append(user_score_combo)
        return sorted(userscores, key=lambda x: x[1])[::-1][:10]
        
        
def add_user_to_leaderboard(username, score):
    leader_data = get_leaderboard()
    with open('data/leaderboard.txt', 'a') as leaderboard:   
        if not (username, score) in leader_data:
            leaderboard.write('\n{}:{}'.format(str(username), str(score)))
        

    
  

"""HOME PAGE"""
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", page_title="Home page")
"""HOME PAGE END"""

"""Pre_Game Page"""
@app.route('/pre_game/', methods=["GET", "POST"])
def pre_game():
        form_data = request.form
        user = form_data['username']
        return render_template("pre_game.html", page_title="Are you ready?", username=user)
"""End Pre_Game Page"""


"""Start of quiz page """
@app.route('/quiz/<username>', methods=["GET", "POST"])
def quiz(username):
    
    if request.method=="POST":
        form = request.form
        
        if form.get('question_1') == 'true':
            context = initialize_game(username)
            return render_template('question_template.html', context=context, username=username)
            
        else:
            #get values for other questions
            question_index = int(request.form.get('question_index'))
            question = get_question(question_index)
            score = int(request.form.get('current_score'))
            attempt = int(request.form.get('attempt'))
                
            submitted_answer = request.form.get('submitted_answer')
            correct_answer = question['question_answer']
            correct = submitted_answer == correct_answer
            
            while question_index < 9:
                
                if correct:
                    #if submitted answer is equal to expected answer increment score, keep attempt at 1, get the next question and flash message correct
                    score+=1
                    question_index+=1
                    attempt=1
                    next_question = get_question(question_index)
                    flash('Answer Correct!  Well done!')
                    print('correct')
                else:
                    #If attempt is more than 2, increment question index and reset attempt to 1
                    if attempt >= 2:
                        attempt =1
                        question_index +=1
                        next_question = get_question(question_index)
                        flash("Unlucky! You should head back to the revision section! Your next question awaits...")
                        
                    
                    else:
                        #If failed on first attempt, increment attempt by 1, for a second chance
                        attempt +=1
                        next_question = get_question(question_index)
                        flash("Oh no... '{}' isn\'t the correct answer! Try again...".format(submitted_answer))
                    
                print(next_question)
                print(question_index)
                if next_question is not None:
                    context = {
                        'question_index' : question_index,
                        'current_score' : score,
                        'question': next_question['question_text'],
                        'answer': next_question['question_answer'],
                        'decoy_answer_1' : next_question['decoy_answer_1'],
                        'decoy_answer_2' : next_question['decoy_answer_2'],
                        'decoy_answer_3' : next_question['decoy_answer_3'],
                        'username' : username,
                        'attempt' : attempt,
                    }
                    print("We're in the if block")
                    return render_template("question_template.html", page_title="Quiz", context = context)
                
                else:
                    print("We're in the else block")
                    session.pop('_flashes', None) #clear flash msgs for next game!
                    add_user_to_leaderboard(username, score)
                    return redirect("leaderboard")
            
            



@app.route('/revise')     
def revise():
    return render_template("revise.html", page_title="Study Center")
    
    
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", page_title="How do you compare?", leaderboard = get_leaderboard())
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)
  