import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if user_choice == 'q':
            break
        elif user_choice not in options:
            print("Invalid input. Please enter a valid choice.")
            continue
        computer_choice = random.choice(options)
        print("Computer chose:", computer_choice)
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")

rock_paper_scissors()