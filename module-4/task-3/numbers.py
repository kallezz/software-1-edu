numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        print(f"Smallest number: {min(numbers)}\nLargest number: {max(numbers)}")
        break

    numbers.append(float(user_input))