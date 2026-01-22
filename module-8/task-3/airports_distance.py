import mysql.connector
from geopy.distance import geodesic

db = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='lentopeli',
         password='lentokone',
         autocommit=True
)

def get_airport_coordinates(icao_code):
    cursor = db.cursor()

    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;"

    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    return result


def run_airport_distance():
    airport1 = input("Enter the ICAO code of the first airport: ").upper()
    airport2 = input("Enter the ICAO code of the second airport: ").upper()

    if not get_airport_coordinates(airport1):
        print(f"Airport with ICAO code {airport1} not found in the database.")
        return
    elif not get_airport_coordinates(airport2):
        print(f"Airport with ICAO code {airport2} not found in the database.")
        return

    result = geodesic(get_airport_coordinates(airport1), get_airport_coordinates(airport2))

    print(f"\n\nDistance between {airport1} and {airport2}: {result.kilometers:.2f} kilometers")

run_airport_distance()