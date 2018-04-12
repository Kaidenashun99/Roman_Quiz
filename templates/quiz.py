def user_menu():
    print("1.Take the quiz")
    print("2.Add your own questions")
    print("3.View the Leaderboard")
    print("4.Exit Game")
    
    option = input("Enter your option:  ")
    return option


#function that allows user to add a question
#to our list of quetions
def add_question():
    print("")
    question = input("Please enter your question:")
    
    print("")
    print("")
    answer = input("{0}\n>".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
def ask_questions():
    questions = []
    answers= [] 
    
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()

    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
   
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("Correct!")
            print("Your current score:")
            print(score)
        else:
            print("Inccorect!")
            print("The correct answer is as follows:")
            print(answer)
            print("Your current score:")
            print(score)
        
    print("You got {0} correct out of a possible {1}.".format(score, number_of_questions))


def quiz_loop():
    while True:
        option = user_menu()
        if option == "1" :
            ask_questions()
        elif option == "2" : 
            add_question()
        elif option == "3" :
            print("You selected 'View the leaderboard'")
        elif option == "4" :
            break
        else:
            print("Invalid option, please select one of the above...")
        print("")


quiz_loop()