# Set up the Flask Weather App
# Import dependencies
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world ():
    return 'hello world'