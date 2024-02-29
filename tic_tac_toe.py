import random

def get_user():
    while True:
        user=input("Enter your choice (rock, paper, or scissors): ").lower()
        if user in ['rock', 'paper', 'scissors']:
            return user
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user==computer:
        return "It's a tie!"
    elif (user=='rock' and computer=='scissors') or (user=='paper' and computer=='rock') or (user=='scissors' and computer=='paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user=get_user()
        computer=get_computer()
        print("You chose:",user)
        print("Computer chose:",computer)
        print(determine_winner(user,computer))
        
        c=0
        while True:
            play_again=input("Do you want to play again? (yes/no): ").lower()
            if play_again=='no':
                c=1
                print("Thanks for playing!")
                break
            elif play_again!='yes':
                print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                break
        if(c==1):
            break
if __name__=="__main__":
    play_game()
