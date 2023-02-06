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

repeat_game = True
count_games = 0
total_count = []

while repeat_game == True:
    count_games += 1

    generated_num = []
    while True:
        random_number = random.choice(range(1,10))
        if str(random_number) in generated_num:
            continue
        else:
            generated_num.append(str(random_number))
        if len(generated_num) == 4:
            break

    # print(generated_num)
    
    print("Enter a 4 digit number: ")
    print(delimiter)

    count = 0
    game_runs = True

    start = datetime.datetime.now()
    while game_runs:
        count +=1 
        
        while True:
            guess_number = str(input(f">>> "))
            if guess_number.isdigit() and len(guess_number) != 4:
                print("You did not input 4 digits.")
            elif guess_number.startswith("0"):
                print("Your number can not start with 0.")
            elif not guess_number.isdigit():
                print("You did not input a numbers.")
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

        final_num = []
        for x in guess_number:
            final_num.append(x) 

        bulls = int()
        cows = int()
        for num in final_num:
            if num in generated_num:
                if num == final_num[0] == generated_num[0]:
                    cows += 0
                    bulls += 1
                elif num == final_num[1] == generated_num[1]:
                    cows += 0
                    bulls += 1
                elif num == final_num[2] == generated_num[2]:
                    cows += 0
                    bulls += 1
                elif num == final_num[3] == generated_num[3]:
                    cows += 0
                    bulls += 1
                else:
                    cows += 1
                    bulls += 0
            else:
                cows += 0
                bulls += 0

        print(f"{bulls} bulls, {cows} cows")
        print(delimiter)
    
        if bulls == 4:
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
            end = datetime.datetime.now()
            time = end - start
            print(f"You did it in {time}")
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
        






    





    

