# app run using port = 80, escape ()

from flask import Flask
from markupsafe import escape  

app = Flask(__name__)

@app.route('/')  
def hello_world():
    return "hello world"

@app.route('/')                             # html                       
def hello(name):
    return f"hello, {escape(name)}!"     # to prevent injection of codes <scripts>

if __name__ == '__main__':  
    app.run(debug=True, host='0.0.0.0', port=80) 