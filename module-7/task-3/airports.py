airports = {}

def main():
    while True:
        print("\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit""")

        chosen_opt = int(input("Please choose an option (1-3): "))

        if chosen_opt == 1:
            icao = input("Enter the ICAO code: ")
            airports[icao] = input("Enter the airport name: ")
            print(f"Airport {airports[icao]} with ICAO code {icao} has been added.")
            continue
        elif chosen_opt == 2:
            icao = input("Enter the ICAO code: ")

            if icao in airports:
                print(f"The airport with ICAO code {icao} is {airports[icao]}.")
            else:
                print(f"No airport found with ICAO code {icao}.")

            continue
        elif chosen_opt == 3:
            print("Thank you for using the Airport Data Management system. Goodbye!")
            break

main()
