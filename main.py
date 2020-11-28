from flask import Flask, render_template

# Importing simply to remove the GET /favicon issue
from flask import send_from_directory

import os
import sys

app = Flask(__name__)

# Index.html Route


@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')


@app.route('/Stat')
def stat():
    return render_template('/stat.html')


# Use export FLASK_APP=main
# Then, export FLASK_ENV=development
# Then, flask run
if __name__ == '__main__':
    app.run(debug=True)

# Loop through categorie and display in navbar.
# for category in

# Remedy GET /favicon issue


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
