import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='dbuser',
    password='123456',
    autocommit=True
    )

def get_airport_infor(iso_country):
    sql = f"select type, name from airport where iso_country = '{iso_country}' order by type asc, name asc;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

prompt = '\nPlease enter the area code of the country:'
prompt += '\n(Enter "q" to quit)\n'

iso_country = input(prompt)
while iso_country != 'q':
    airport_infor = get_airport_infor(iso_country.upper())

    index = 0
    while airport_infor:
        airport_type = airport_infor[index][0]
        airport_name = airport_infor[index][1]

        print(f"{airport_type}: {airport_name}")

        index += 1
        if index == len(airport_infor):
            break

    iso_country = input(prompt)