# Hyttiluokkalista
classes = {
    "LUX": "Upper-deck cabin with a balcony.",
    "A": "Above the car deck, equipped with a window.",
    "B": "Windowless cabin above the car deck.",
    "C": "Windowless cabin below the car deck."
}

class_input = input("Enter the cabin class (LUX, A, B, or C): ")

# if class_input in classes:
#     print(classes[class_input])
# else:
#     print("Invalid cabin class.")
# Moodlelle ei kelvannut, halusi käyttää elif tyyliä

if class_input == "LUX":
    print(classes[class_input])
elif class_input == "A":
    print(classes[class_input])
elif class_input == "B":
    print(classes[class_input])
elif class_input == "C":
    print(classes[class_input])
else:
    print("Invalid cabin class.")
