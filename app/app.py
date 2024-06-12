from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/fizzbuzz")
    def fizzbuzz():
        return render_template('fizzbuzz.html')
    
    return app