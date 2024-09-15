import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='dbuser',
    password='123456',
    autocommit=True
    )

def get_airport_name(airport_ident):
    sql = f"SELECT name FROM airport WHERE ident='{airport_ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    name = result[0][0]
    return name

def get_airport_location(airport_ident):
    sql = f"SELECT municipality FROM airport WHERE ident='{airport_ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    location = result[0][0]
    return location

prompt = "\nPlease enter the ICAO code for the airport:\n"
prompt += f"(Press 'q' to quit)\n"
airport_ident = input(prompt)
while airport_ident != 'q':
    print(f"The airport for ICAO '{airport_ident.upper()}' is '{get_airport_name(airport_ident)}', " 
          f"which is located at '{get_airport_location(airport_ident)}'.")
    airport_ident = input(prompt)
