import random

def play():
    wins = 0
    losses = 0

    while True:
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        user_choice = input("Enter a choice (rock, paper, scissors): ")
        
        if user_choice in options:
            if user_choice.lower() == computer_choice:
                print("Tie")
                wins = wins
                losses = losses
            elif user_choice.lower() == "rock" and computer_choice == "scissors":
                print("You win!")
                wins += 1
            elif user_choice.lower() == "paper" and computer_choice == "rock":
                print("You win!")
                wins += 1
            elif user_choice.lower() == "scissors" and computer_choice == "paper":
                print("You win!")
                wins += 1
            else:
                print("You lose!")
                losses += 1
        else:
            print("Invalid choice")
        print(f"Wins: {wins}, Losses: {losses}")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

play()