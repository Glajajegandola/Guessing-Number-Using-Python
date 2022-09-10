# Mini Project No.2 using Python

import random 
play_again = "Yes"
score = 0

print("Welcome to the Mini games")

The_range = input("Type your number range to guess (Must be greater than 5): ")

if The_range.isdigit():
    The_range = int(The_range)
    random_number = random.randint(0, The_range)
   
    if The_range <= 5:
        print("Please choose greater than 5, restart the program to play again")
      
else:
    print("Please type a number, restart the program to play again")
    quit()

while True: 

    while True: 
        user_guess = input("What's is your guess? ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("We only accept number")
            continue

        if user_guess == random_number:
            print("Your guess is correct!")
            score += 1
            break             
        else: 
            print("Your guess is wrong!")

    play_again = input("Your Current Score is: " + str(score) + " / " + "Would you like to play again? (Yes or No): ")

    if play_again == "Yes":
        print("Ok, Let's play again!")
        The_range = input("Type your number range to guess: ")
        The_range = int(The_range)
        random_number = random.randint(0, The_range)
        continue

    if The_range <= 5:
        print("Please choose greater than 5, restart the program to play again")
        break
        
    else:
        print("Thanks for playing, Goodbye")
        break
