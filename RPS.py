import random
import time
blank = """                 
             























          
    
    

























"""
line = "====================="
welcome = "       WELCOME"

    

def main():
    print(welcome)
    print(line)
    print("     Play Game (1)")
    print("     Rules (2)")
    print("     Credits (3)")
    print("     Quit (4)")
    selection = input("Select Option: ")
    if selection == "1":
        game()
    if selection == "2":
        rules()
    if selection == "3":
        credits()
    if selection == "4":
        exit()
    else:
        main()


def rules():
    print(blank)
    print("its Rock Paper Scissors, its not that hard")
    input("")
    print(blank)
    main()
def exit():
    quit()

def credits():
    print(blank)
    print("A small program made by J_West_San")
    input("")
    print(blank)
    main()

def game():
    ran = random.randint(1, 3)
    if ran == 3:
        answer = "p"
    if ran == 2:
        answer = "r"
    if ran == 1:
        answer = "s"
    print(blank)
    print("Rock, Paper or Scissors")
    player_answer = input("Input your choice: ")
    if player_answer == 'Rock'or 'rock':
        if answer == 'p':
            print("Computer Chose Paper")
            time.sleep(1)
            print("You Lose..")
            play_again()
        if answer == 'r':
            print("Computer Chose Rock")
            time.sleep(1)
            print("Tie!")
            play_again()
        if answer == 's':
            print("Computer Chose Scissors")
            time.sleep(1)
            print("You Win!!")  
            play_again()
    if player_answer == 'Paper'or 'paper':
        if answer == 'p': 
            print("Computer Choses Paper")
            time.sleep(1)
            print("Tie!")
            play_again()
        if answer == 'r':
            print("Computer Choses Rock")
            time.sleep(1)
            print("You Win!!")
            play_again()
        if answer == 's':
            print("Computer Choses Scissors")
            time.sleep(1)
            print("You Lose..")
            play_again()  
    if player_answer == 'Scissors'or 'scissors':
        if answer == 'p':
            print("Computer Choses Paper")
            time.sleep(1)
            print("You Win!!")
            play_again()
        if answer == 'r':
            print("Computer Choses Rock")
            time.sleep(1)
            print("You Lose..")
            play_again()
        if answer == 's':
            print("Computer Choses Scissors")
            time.sleep(1)
            print("Tie!")
            play_again()
    else:
        player_answer = input("invalid prompt, please try again: ")
def play_again():
    input("")
    main()
main()

        
    


    






