from flask import Flask, render_template
import front_matter as fm
import pprint as pp
from get_note_content import get_note_content

# Remove the GET /favicon issue
from flask import send_from_directory


import os
import sys

import categories as cat

# Get the category files
category_files = cat.categories

# Drop MLProjects for now.
if 'Machine Learning' in category_files.keys():
    del category_files['Machine Learning']

# Set the dictionary of note links mapping to metadata
note_dict = fm.generate_note_dict(category_files)

# Initialize Flask
app = Flask(__name__)

# Favicon 
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Index.html, homepage Route
@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')


# Data Science Route

@app.route('/data-science')
def data_science():
    return render_template('/category-indices/data-science.html', title='Data Science', description='Data science. Statistics.  TensorFlow, Pandas, Sci-Kit Learn, and so much more!  This page will house all of my personal notes.  Additionally, I will post some external resources which I have found helpful.', image_route='static/assets/media/stat-homepage-violin-plots.png', get_note_content = get_note_content, category_files=category_files['Data Science'], note_dict=note_dict)

data_sci_title_dict = {}
for file in category_files['Data Science']: 
    title = note_dict[file]['title']
    content = get_note_content(file)
    data_sci_title_dict[title] = content

# Data Science Notes Route
@app.route('/data-science-notes/<note_title>')
def note(note_title):   
    return render_template('notes.html', note_title = note_title, title_content_dict=data_sci_title_dict)



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


# export FLASK_APP=main FLASK_ENV=development
# flask run

# Remedy GET /favicon issue


if __name__ == '__main__':
    app.run(port=5000)
