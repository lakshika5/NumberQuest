import random

def number_guessing_game():
    print(".........WELCOME TO THE NUMBER GUESSING GAME......")
    print()
    a = int(input("enter the lower bound of the range : "))        #lower bound - a
    b = int(input("enter the upper bound of the range : "))         #upper bound - b

    
    secret_number = random.randint(a,b)
    guess = None
    attempts = 0

    
    print(f"Guess the number between the range you have provided : ")

    
    while secret_number != guess:
        guess = int(input("enter your guess : "))
        attempts += 1
        
        if guess > secret_number:
            print("your guess is too high ! ")
        elif guess < secret_number:
            print("your guess is too low ")
        else:
            print(f".......CONGRATULATIONS ! YOUR GUESS IS CORRECT IN  {attempts} ATTEMPTS..................")
        

number_guessing_game()



print("Wanna Play Again ? ")
output = input("yes or no : ").lower()


if (output != "yes"):
    print("HAVE A NICE DAY !")
else:
    number_guessing_game()
    
