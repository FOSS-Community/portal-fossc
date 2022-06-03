from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "<center> <h1> Welcome to FOSSC Portal </h1> </center>"