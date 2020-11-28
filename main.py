from flask import Flask, render_template
import os
import sys

app = Flask(__name__)

# Index.html Route


@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')


# Use export FLASK_APP=main
# Then, export FLASK_ENV=development
# Then, flask run
if __name__ == '__main__':
    app.run(debug=True)

# Loop through categorie and display in navbar.
print(os.listdir('/categories'))
# for category in
