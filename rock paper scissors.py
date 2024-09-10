import random
import string

def comp():
    l1=['rock','paper','scissors']
    return random.choice(l1)

def user():
    while True:
        l2=input("Enter your choice: \nrock\npaper\nscissors\n\n").lower()
        if l2 in ['rock', 'paper', 'scissors']:
            return l2
        else:
            print("Invalid choice, Try Again")
            
def game(user,comp):
    if user == comp:
        return "It's a Tie! :|\n"
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'scissors' and comp == 'paper') or \
         (user == 'paper' and comp == 'rock'):
        return "YOU WON! :)\n"
    else:
        return "YOU LOSE :(\n"

print ("***WELCOME TO ROCK PAPER SCISSORS***\n")
print ("In this game there are three choices - Rock,paper and scissors.\nThe user must choose their selection and \
the computer will randomly select its choice.\n\nLogic of the game:\n#Rock beats scissors.\n#Scissors beats paper.\n#paper beats rock.\n")
while True:
    comp_choice = comp()
    user_choice = user()
    result = game(user_choice, comp_choice)

    print(f'\nYou chose: {user_choice}')
    print(f'computer chose :{comp_choice}')
    print("\n")
    print(result)

    again = input("Do you want to play again ? (yes/no): ").lower()
    if again != 'yes':
        break
    print("\n")
print("Thank you for playing\n Hope you Enjoyed it :)")
    
    
