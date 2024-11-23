import json
import mysql.connector
from flask import Flask

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='dbuser',
    password='123456',
    autocommit=True,
    )

app = Flask(__name__)
@app.route('/airport/<ICAO>')

def return_airport_info(ICAO):
    try:
        ICAO = ICAO.upper()

        cursor = connection.cursor()
        sql = f"""
        SELECT name, municipality
        FROM airport
        WHERE ident = "{ICAO}";
        """
        cursor.execute(sql)
        result = cursor.fetchall()

        name = result[0][0]
        location = result[0][1]

        response = {
            "ICAO": ICAO,
            "Name": name,
            "Location": location
        }

        response = json.dumps(response)
        return response

    except IndexError:
        response = {
            "message": "Invalid ICAO",
            "status": 400
        }

        response = json.dumps(response)
        return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)