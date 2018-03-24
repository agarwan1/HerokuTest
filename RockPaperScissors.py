# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]
wins = {
    'r': 's',
    'p': 'r',
    's': 'p'
}

# Computer Selection
computer_choice = random.choice(options)
print("computer chose: " + computer_choice )
# User Selection
go_on = 'Y'
while go_on == 'Y':
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ").lower()
    if not user_choice in options:
        continue

    if user_choice == computer_choice:
        print("Draw")
    elif computer_choice == wins[user_choice]:
        print("Win")
    else:
        print("Lost")
    go_on = input("Go on? (y/N)").upper()