from flask import Flask 
app = Flask (__name__)

@app.route('/')
def Hello_world():
    return 'Hello Marie'
if __name__ == '__main__':
    app.run(debug=True) 