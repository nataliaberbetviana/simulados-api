# app.py
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')