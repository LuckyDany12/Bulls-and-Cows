"""
Bulls and cows.py: second project in Engeto online python academy

author: Daniela Horucková
email: horuckova.d@seznam.cz
discord: LuckyDany#2774
"""

import random
import datetime

delimiter = "-" * 48

print(f"""Hi there! Wellcome. 
{delimiter}
I've generated a random 4 digit number for you. 
Let's play a bulls and cows game.
{delimiter}""")

def correct_number(generated_number: list, final_number: list) -> int:
    bulls = int()
    for num in final_number:
        if num == final_number[0] == generated_number[0]:
            bulls += 1
        elif num == final_number[1] == generated_number[1]:
            bulls += 1
        elif num == final_number[2] == generated_number[2]:
            bulls += 1
        elif num == final_number[3] == generated_number[3]:
            bulls += 1
        else:
            bulls += 0
    return bulls

def contains_number(generated_number: list, final_number: list) -> int:
    cows = int()
    for num in final_number:
        if num in generated_number:
            cows += 1
        else:
            cows += 0
    return cows

repeat_game = True
count_games = 0
total_count = []

while repeat_game == True:
    count_games += 1

    generated_number = []
    while True:
        random_number = random.choice(range(1,10))
        if str(random_number) in generated_number:
            continue
        else:
            generated_number.append(str(random_number))
        if len(generated_number) == 4:
            break

    # print(generated_number) = you can remove this line comment 
    #   if you want to know generated number
    
    print("Enter a 4 digit number: ")
    print(delimiter)

    count = 0
    game_runs = True

    while game_runs:
        count +=1 
        start = datetime.datetime.now().second
       
        while True:
            guess_number = str(input(f">>> "))
            if guess_number.isdigit() and len(guess_number) != 4:
                print("You did not input 4 digits.")
            elif guess_number.startswith("0"):
                print("Your number can not start with 0.")
            elif not guess_number.isdigit():
                print("You did not imput a numbers.")
            elif guess_number.isdigit():
                guess = []
                for x in guess_number:
                    if x in guess:
                        print("Number must not contain duplicates.")
                        break
                    else:
                        guess.append(x)
                if len(guess) == 4:
                    break

        final_number = []
        for x in guess_number:
            final_number.append(x) 

        bulls = correct_number(generated_number,final_number)
        cows = contains_number(generated_number,final_number)
        print(f"{bulls} bulls, {cows} cows")
        print(delimiter)
    
        if bulls == 4:
            end = datetime.datetime.now().second
            print(
                f"Correct. You've guessed the right number\n"
                f"in {count} guesses!"
                )
            if count <= 8:
                print("That's amazing!")
            elif count > 8 and count <= 12:
                print("That's average.")
            else:
                print("Not so good. :(")
            
            total_count.append(count)
            print(f"You did it in {end - start} seconds.")
            print(delimiter)
            game_runs = False

    repeat = input("Do you want to play again? y/n: ")
    if repeat == "y":
        continue

    else:
        repeat_game = False
        print(
            f"You played {count_games} games,\n"
            f"total number of guesses: {sum(total_count)}."
            )
        






    





    

