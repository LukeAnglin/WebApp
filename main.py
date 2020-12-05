from flask import Flask, render_template
from categories import generate_note_dict
import pprint as pp
from categories import get_note_content
from categories import title_dict

# Remove the GET /favicon issue
from flask import send_from_directory


import os
import sys

import categories as cat

# Get the category files
category_files = cat.categories

# Set the dictionary of note links mapping to metadata
note_dict = cat.note_dict

# Initialize Flask
app = Flask(__name__)

# Favicon issue resolution


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Homepage Route


@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')

# CATEGORY ROUTES

# To create a route for a category, create a dictionary with the following parameters:
    # title - Category title
    # description - What does this category show?
    # image_route - Image to be displayed as the category's logo of sorts
    # get_note_content - an obligatory function for parsing HTML files
    # category_files - should resemble category_files[<category title goes here>]
    # note_dict - Also necessary, simply pass in note_dict = note_dict

# Route parameters to be unpacked in category homepages

data_sci_route_params = {
    'title': 'Data Science Foundations',

    'description': 'Data science. Python, Pandas, Sci-Kit Learn, and so much more!  This page will house all of my personal notes.  Also note that this will contain resources mostly in the Machine Learning subset of data science, whereas Deep Learning will have a unique category. Additionally, I will post some external resources which I have found helpful.',

    'image_route': 'static/assets/media/stat-homepage-violin-plots.png',

    'get_note_content': get_note_content,

    'category_files': category_files['Data Science'],

    'note_dict': note_dict,

}
deep_learning_route_params = {
    'title': 'Deep Learning',

    'description': 'Neural networks!  Keras and Tensorflow allow us to build incredible models, capable of more than we can imagine.  Let\'s learn how to use, visualize and evaluate this sector of data science!',

    'image_route': 'static/assets/media/deep_homepage.jpg',

    'get_note_content': get_note_content,

    'category_files': category_files['Deep Learning'],

    'note_dict': note_dict,

}

notebook_reference_route_params = {

    'title': 'Notebook Reference',

    'description': 'The majority of content here will consist of Jupyter Notebooks.  These are best for note-taking and presentation.  Note that Python scripts are preferable in some cases, but for the sake of readability and experimentation, I choose Jupyter Notebooks for this.  I also have .py scripts in my GitHub repository for different modules and packages I have created myself.',

    'image_route': 'static/assets/media/ml-category-homepage.png',

    'get_note_content': get_note_content,

    'category_files': category_files['Notebook Reference'],

    'note_dict': note_dict,
}

# First, initialize a dictionary containing the content of the title you gave your category.  Here's an example:

data_sci_title_dict = title_dict['Data Science']

# To initialize a routes for notes, pass in the following **kwargs in a similar manner as we did for category routes.
# title_dict = <the title dictionary you just created goes here>
data_sci_notes_params = {
    'title_dict': data_sci_title_dict,
}

deep_learning_title_dict = title_dict['Deep Learning']
deep_learning_notes_params = {
    'title_dict': deep_learning_title_dict,
}

# Then, unpack that dictionary in the render-template. Additionally, place the **kwarg note_title=note_title before the dictionary unpacking step.

# Then, to create the route, use render template, passing in the template file as a positional argument, and unpack the dictionary for the **kwargs to be used in rendering the page

# NAMING CONVENTION - Lower case of the folder name in the categories directory
# ALPHABETIZE!
# EXAMPLE - 'Data-Science' folder should be '/data-science' route

# CATEGORY PAGE ROUTES


@app.route('/data-science')
def data_science():
    return render_template('/category-indices/data-science.html', **data_sci_route_params)

@app.route('/notebook-reference')
def notebook_reference():
    return render_template('/notebook-reference.html', **notebook_reference_route_params)

@app.route('/deep-learning')
def deep_learning():
    return render_template('/category-indices/deep-learning.html', **deep_learning_route_params)

# Deep Learning Notes

# @app.route('/js')

# @app.route('/linear-algebra')

# @app.route('/r')

# @app.route('/stat-and-probability')


# NOTES ROUTES


@app.route('/data-science-notes/<note_title>')
def data_sci_note(note_title):
    return render_template('notes.html', note_title=note_title, **data_sci_notes_params)

@app.route('/deep-learning-notes/<note_title>')
def deep_learning_note(note_title):
    return render_template('notes.html', note_title=note_title, **deep_learning_notes_params)

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
