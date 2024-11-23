from flask import Flask
import json

app = Flask(__name__)

@app.route('/prime_number/<number>')

def isPrime(number):
    try:
        number = int(number)
        is_prime = True

        if number <= 1:
            is_prime = False
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False

        response = {
            "Number": number,
            "isPrime": is_prime,
        }
        response = json.dumps(response)

        return response

    except ValueError:
        response = {
            "message": "Invalid number",
            "status": 400
        }
        response = json.dumps(response)
        return response

if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port = 5000)