import mysql.connector

db = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='lentopeli',
         password='lentokone',
         autocommit=True
)

def get_airports_by_country(iso_country):
    cursor = db.cursor()

    query = "SELECT type, COUNT(*) AS count FROM airport WHERE airport.iso_country = %s GROUP BY type;"

    cursor.execute(query, (iso_country.upper(),))
    result = cursor.fetchall()

    return result


def run_country_program():
    country_input = input("Enter the country code (e.g., FI for Finland): ")


    results = get_airports_by_country(country_input)

    if not results:
        print(f"No airports found for country code '{country_input.upper()}' or database connection failed.")
        return

    print(f"\n\nAirports in {country_input}:")

    for result in results:
        if result[0] == "closed":
            continue

        print(f"{result[1]} {result[0]} airports")

run_country_program()