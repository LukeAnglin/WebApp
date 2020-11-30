from flask import Flask, render_template

# Importing simply to remove the GET /favicon issue
from flask import send_from_directory

import os
import sys

import categories as cat

categories = cat.categories

# Initialize Flask
app = Flask(__name__)

# Index.html, homepage Route


@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')


# Data Science Route

data_science_files = categories['Data Science']
print(data_science_files)


@app.route('/category_indices/data-science')
def data_science():
    return render_template('/category-indices/data-science.html', title='Data Science', description='Data science. Statistics.  TensorFlow, Pandas, Sci-Kit Learn, and so much more!  This page will house all of my personal notes.  Additionally, I will post some external resources which I have found helpful.', image_route='static/assets/media/stat-homepage-violin-plots.png', route='data_science')

# Machine Learning Projects


@app.route('/machine-learning')
def machine_learning():
    return render_template('/category-indices/machine-learning.html')

# Python Route


@app.route('/python')
def python():
    return render_template('/category-indices/python.html')

# Linear Algebra Route


# JS Route


# Use export FLASK_APP=main
# Then, export FLASK_ENV=development
# Then, flask run

# Loop through categorie and display in navbar.
# for category in

# Remedy GET /favicon issue


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
