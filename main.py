from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0') # necessario para rodar no container
