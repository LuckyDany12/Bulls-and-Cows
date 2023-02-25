"""
Bulls and cows.py: second project in Engeto online python academy

author: Daniela Horucková
email: horuckova.d@seznam.cz
discord: LuckyDany#2774
"""

import random
import datetime

delimiter = "-" * 48

print(
    f"""Hi there! Welcome. 
{delimiter}
I've generated a random 4 digit number for you. 
Let's play a bulls and cows game.
{delimiter}"""
)

repeat_game = True
count_games = 0
total_count = []


def generate_number():
    random_number = random.sample(range(1, 10), 4)
    return random_number


while repeat_game == True:
    count_games += 1

    generated_num = generate_number()

    # print(generated_num)
    print("Enter a 4 digit number: ")
    print(delimiter)

    count = 0
    game_runs = True
    start = datetime.datetime.now()

    while game_runs:
        count += 1

        while True:
            guess_number = str(input(f">>> "))
            if guess_number.isdigit() and len(guess_number) != 4:
                print("You did not input 4 digits.")
            elif guess_number.startswith("0"):
                print("Your number can not start with 0.")
            elif not guess_number.isdigit():
                print("You did not input a numbers.")
            elif len(set(guess_number)) != 4:
                print("Number must not contain duplicates.")
            else:
                break

        final_num = []
        for i in guess_number:
            num = int(i)
            final_num.append(num)

        bulls = int()
        cows = int()
        for i, num in enumerate(final_num):
            if num == generated_num[i]:
                bulls += 1
            elif num in generated_num:
                cows += 1

        print(f"{bulls} bulls, {cows} cows")
        print(delimiter)

        if bulls == 4:
            print(f"Correct. You've guessed the right number\n" 
                  f"in {count} guesses!")
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

        






    





    

