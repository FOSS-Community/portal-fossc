from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "<center> <h1> Welcome to FOSSC Portal </h1> </center>"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":

    app.run(debug=True)