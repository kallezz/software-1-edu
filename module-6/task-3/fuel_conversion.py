def gallons_to_liters(gallons):
    return gallons * 3.785

gallons_input = 1.0

while gallons_input > 0:
    gallons_input = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallons_input > 0:
        print(f"{gallons_input} American gallons is {gallons_to_liters(gallons_input):.2f} liters.")
else:
    print("Program finished.")