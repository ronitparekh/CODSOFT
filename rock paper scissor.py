import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

def main():
    user_score = 0
    computer_score = 0
    play_again = True
    
    print("Welcome to Rock-Paper-Scissors!\n")
    
    while play_again:
        result = play_game()
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        print(f"\nScore - You: {user_score} | Computer: {computer_score}\n")
            
        play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
        play_again = play_again_input == 'yes'

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
