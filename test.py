from flask import Flask 
from markupsafe import escape
app = Flask (__name__)

@app.route('/')
def Hello_world(name):
    return f'hello, {escape(name)}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80) 


