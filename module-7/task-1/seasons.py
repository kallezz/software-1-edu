seasons = {
    "winter": {
        "display_name": "winter",
        "months": [12, 1, 2]
    },
    "spring": {
        "display_name": "spring",
        "months": [3, 4, 5]
    },
    "summer": {
        "display_name": "summer",
        "months": [6, 7, 8]
    },
    "autumn": {
        "display_name": "autumn",
        "months": [9, 10, 11]
    },
}

def get_season(month_num):
    for season in seasons.values():
        if month_num in season["months"]:
            return season["display_name"]

    return None


month_input = int(input("Enter the number of a month (1-12): "))
print(f"You entered: {month_input}")

if month_input in range(1, 13):
    print(f"The season is {get_season(month_input)}.")
else:
    print("Please enter a number between 1 and 12.")
