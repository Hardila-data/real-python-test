# Hello world flask

#import flask clss from the flask package
from flask import Flask

#Create and application object
app = Flask(__name__)

#Error handling
app.config["DEBUG"] = True

# Use the decorator pattern to 
# link the view function to url
@app.route("/")
@app.route("/hello")

# Define the view function
def hello_world():
    return "Hello, World!"

@app.route("/integer/<int:value>")
def int_type(value):
    print(value+1)
    return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query + " test"

#Start the development server usin run() method
if __name__ == "__main__":
    app.run()