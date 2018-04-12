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
    
    for question, answer in zip(questions, answers):
        guess = input(question + "> ")
        


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