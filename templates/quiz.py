def user_menu():
    print("1.Take the quiz")
    print("2.Add your own questions")
    print("3.View the Leaderboard")
    print("4.Exit Game")
    
    option = input("Enter your option:  ")
    return option
    
def quiz_loop():
    while True:
        option = user_menu()
        if option == "1" :
            print("You selected 'Take the quiz'")
        elif option == "2" : 
            print("You selected 'Add a question'")
        elif option == "3" :
            print("You selected 'View the leaderboard'")
        elif option == "4" :
            break
        else:
            print("Invalid option, please select one of the above...")
        print("")

quiz_loop()