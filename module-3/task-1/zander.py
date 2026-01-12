zander_len = float(input("Enter the length of the zander in centimeters: "))
min_len = 42

if zander_len >= min_len:
    print("The zander meets the size limit.")
else:
    missing_len = min_len - zander_len
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing_len:.1f} centimeters below the size limit.")