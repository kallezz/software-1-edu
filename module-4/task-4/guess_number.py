import random

answer = random.randint(1,10)

while True:
    user_answer = input("Guess a number (1-10): ")

    # Check if int
    try:
        int(user_answer)
    except ValueError:
        print("Invalid input.")
        continue

    if int(user_answer) < answer:
        print("Too low")
    elif int(user_answer) > answer:
        print("Too high")
    else:
        print("Correct")
        break