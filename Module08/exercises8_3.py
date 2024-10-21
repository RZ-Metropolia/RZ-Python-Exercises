import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='dbuser',
    password='123456',
    autocommit=True
    )

def get_airport_name(ident):
    sql = f"select name from airport where ident='{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    name = cursor.fetchall()[0][0]
    return name

def get_airport_coordinate(ident):
    sql = f"select latitude_deg, longitude_deg from airport where ident='{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    coordinate = cursor.fetchall()[0]
    return coordinate

def calculate_distance(coordinate_1, coordinate_2):
    return distance.distance(coordinate_1, coordinate_2).km

while True:
    print("\nLet me calculate the distance between two airport for you!")
    print("(Enter 'q' to quit)")

    airport_1_ident = input("Please enter the ICAO code of the first airport: ")
    if airport_1_ident == 'q':
        exit()
    else:
        airport_1_name = get_airport_name(airport_1_ident)
        airport_1_coordinate = get_airport_coordinate(airport_1_ident.upper())

    airport_2_ident = input("Please enter the ICAO code of the second airport: ")
    if airport_2_ident == 'q':
        exit()
    else:
        airport_2_name = get_airport_name(airport_2_ident)
        airport_2_coordinate = get_airport_coordinate(airport_2_ident.upper())

    result = calculate_distance(airport_1_coordinate, airport_2_coordinate)
    print(f"The distance between {airport_1_name} and {airport_2_name} is {result:.2f} kilometers.")