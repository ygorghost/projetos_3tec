from flask import Flask, render_template

app = Flask(__name__)

def create_app():
    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/fizzbuzz")
    def fizzbuzz():
        return render_template('fizzbuzz.html')
    
    return app