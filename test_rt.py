# Routing + escape + 

from flask import Flask , request
from markupsafe import escape


app = Flask(__name__)

@app.route('/user/<user_name>')
def show_user_profile(username):

    return f'user, {escape (username)}'

if __name__ == '__main__':
    app.run(debug=True)



