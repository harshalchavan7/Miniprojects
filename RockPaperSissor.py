import random

def play():
    user = input("Enter your choice (rock/paper/scissors): ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        return "It's a tie!"
    if is_win(user, computer):
        return "You won!"
    return "You lost!"

def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or \
            (player == 'scissors' and opponent == 'paper') or \
            (player == 'paper' and opponent == 'rock'):
        return True
    return False

if __name__ == "__main__":
    print(play())
