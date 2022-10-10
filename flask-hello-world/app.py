# Hello world flask

#import flask clss from the flask package
from flask import Flask

#Create and application object
app = Flask(__name__)

# Use the decorator pattern to 
# link the view function to url
@app.route("/")
@app.route("/hello")

# Define the view function
def hello_world():
    return "Hello, World!"

#Start the development server usin run() method
if __name__ == "__main__":
    app.run()