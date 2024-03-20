from flask import Flask                     # Hopfully the next few tries work. code not running cause of the mistakes below: (check next .py file for correct codes)

app = Flask(__name__)
@app.route('/')

def hello_world():                           # two def. Hello world
    return "hello world"

if __name__ == '__main--':
    app.run (debug=True)


from markupsafe import escape                   # move all imports to the top for clarity

@app.route('/')                             # i made an error here by giving two route commands
def hello(name):                            # "hello" is different from fist def. "hello world"
    return f"Hello, {escape(name)}!"
