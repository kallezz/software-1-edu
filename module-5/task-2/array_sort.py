values = []


while True:
    input_value = input("Enter a number: ")

    if input_value == "":
        break

    values.append(float(input_value))


values.sort(reverse=True)

print("The greatest numbers in descending order: ")

for i, value in enumerate(values):
    if i > 4:
        break

    print(float(value))