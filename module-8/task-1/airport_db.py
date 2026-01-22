import mysql.connector

db = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='lentopeli',
         password='lentokone',
         autocommit=True
)

def search_db_with_icao():
    cursor = db.cursor()
    icao = input("Enter the ICAO code of an airport: ")

    query = "SELECT airport.name, country.name FROM airport, country WHERE ident = %s AND airport.iso_country = country.iso_country;"

    cursor.execute(query, (icao.upper(),))

    result = cursor.fetchone()

    if not result:
        return f"No airport found with ICAO code {icao}"

    return f"Airport name: {result[0]}\nLocation: {result[1]}"

print(search_db_with_icao())
