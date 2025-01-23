from flask import Flask
import requests

app = Flask(__name__)

BE_URL = "http://dev-be-service:30031/data"
#BE_URL = "http://localhost:30031/data"
@app.route('/send', methods=['GET'])

def send_hello():
    response = requests.get(url = BE_URL)
    print(response.text)
    return response.text
    


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=30030)