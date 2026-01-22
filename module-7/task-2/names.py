names = set()

while True:
    name_input = input()

    if name_input == "":
        break

    if name_input in names:
        print("Existing name")
    else:
        print("New name")

    names.add(name_input)

print(names)
