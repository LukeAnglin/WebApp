import os.path
import pprint as pp
import sys
import requests
from bs4 import BeautifulSoup
import frontmatter
import pprint as pp
from itertools import chain
import os
import categories as cat
from frontmatter.default_handlers import YAMLHandler, TOMLHandler

# The purpose of this file is to add the relevant categories and create a dictionary full of the category mapping to the relevant files.

# Edit the following lines, 8-13, in order to update some of the features.

# Remove certain folders that I don't want
names_to_remove = ['.ipynb_checkpoints']

# Change the names_to_change and new_name arrays to update
names_to_change = ['JS']
new_names = ['JavaScript']

# Create a new dictionary mapping filepaths to meta data from parsed markdown.
note_metadata = {}

# Categories are in the 'categories' folder in the root directory of the project
categories = os.listdir('categories')

# Remove .DS_Store
categories = categories[1:]

# Set the initial categories directory
categories_dir = 'categories'

# Initialize an empty dictionary to store categories mapping to files
category_dict = {}


def create_categories():
    """Fills the 'category_dict' dictionary with categories mapping to filepaths. 
    """
    for category in categories:
        if category == 'MLProjects':
            continue
        category_dir = os.path.join(categories_dir, category)
        category_contents = os.listdir(category_dir)
        # Initialize empty list to store categories mapping to lists of html files (which are dicts)
        category_files = []

        # Loop through files in each category dir
        for note in category_contents:
            if note.endswith('.html'):
                category_files.append(os.path.join(category_dir, note))
        # Map current category to the list of category_files
        category_dict[category] = category_files

    # Loop through the files in the MLProjects/Notes dir
    mlProjects_dir = os.path.join(categories_dir, 'MLProjects/Notes')
    mlProjects_dir_contents = os.listdir(mlProjects_dir)
    ml_notes = []
    for note in mlProjects_dir_contents:
        if note.endswith('.ipynb') or note.endswith('.html'):
            ml_notes.append(os.path.join(
                categories_dir, 'MLProjects', 'Notes', note))
    category_dict['Machine and Deep Learning'] = ml_notes
    return category_dict


def modify_categories(category_dict):
    """Applies multiple modification functions to the overarching categories (ex. Statistics or Data Science, not the filepaths) 

    Args:
        category_dict (dict): A dictionary of categories mapping to filenames  

    Returns:
        dict: The dictionary after applying the modification functions. 
    """
    # Create a copy of the dictionary
    categories = category_dict.copy()

    # Replace dashes keys with spaces
    for category in category_dict.keys():
        new_cat_name = category.replace('-', ' ')
        categories[new_cat_name] = categories.pop(category)

    # Replace names with ones better suited for headings
    for old_name, new_name in zip(names_to_change, new_names):
        categories[new_name] = categories.pop(old_name)

    # Remove names that I don't want
    for name in names_to_remove:
        if name in categories:
            del categories[name]

    return categories


def get_note_content(html_file):
    """Get's the content of a note

    Args:
        html_file (str): The file (meaning the relative file path) to be parsed.  Should be of .html extension 
    """
    try:
        html_content = open(html_file, 'r')
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find("div", {"class": "note-content"})
    except FileExistsError:
        return f"Failed to find file {html_file}"


def fetch_note_meta(filepath: str) -> dict:
    """Takes a filepath and returns a dictionary mapping the filepath to the metadata from a .md file.  Looks for the frontmatter in the .md file.  

    Args:
        filepath (str): The path of the file being parsed

    Returns:
        dict: A dictionary mapping the filepath to the metadata from a .md
    """
    if os.path.isfile(filepath):
        with open(filepath) as file:
            note = frontmatter.load(file)
        return dict(note)
    else:
        return {'publish': False}


def generate_note_dict(category_dict: dict) -> dict:
    """Generates a dictionary of dictionaries mapping notes filepaths to their respective metadata

    Args:
        category (dict): A dictionary of the categories and their files/notes

    Returns:
        dict: A list of filepaths corresponding to the notes mapping to metadata 
    """
    # Store values of the dict in a list
    notes = list(category_dict.values())
    # Flatten list
    notes = list(chain(*tuple(notes)))

    # Initialize empty list to hold dictionaries
    notes_meta = {}
    # Iterate through flattened list of notes.  Create a list of dictionaries mapping note
    for note in notes:
        original_html = False
        original_ipynb = False
        if note.endswith('.html'):
            original_html = True
        if note.endswith('.ipynb'):
            original_ipynb = True
        # Remove the file extension
        note = os.path.splitext(note)[0]

        # Add '.md' extension
        note = note + '.md'

        # Only do the following IFF the file exists!
        try:

            # Fetch yaml data, and append the meta dictionary to the notes_meta dictionary
            notes_meta[note] = fetch_note_meta(note)

            if original_html:
                # Remove '.md' ext
                noteNewName = os.path.splitext(note)[0]

                # Add '.html' ext back
                noteNewName = noteNewName + '.html'

                # Change key-name
                notes_meta[noteNewName] = notes_meta.pop(note)

            if original_ipynb:
                # Remove '.md' ext
                noteNewName = os.path.splitext(note)[0]

                # Add '.ipynb' ext back
                noteNewName = noteNewName + '.ipynb'

                # Change key-name
                notes_meta[noteNewName] = notes_meta.pop(note)
        # Do nothing if the .md file doesn't exist which stores metadata
        except FileNotFoundError:
            pass

    # Return the dictionary of dictionaries
    return notes_meta


# Create the categories
create_categories()

# Categories stores a category ('Data Science') mapping to available files ('Sets.html')
categories = modify_categories(category_dict)

# Generates a note dictionary ('Sets.html') mapping filepaths to metadata  {title: 'Sets'}
note_dict = generate_note_dict(categories)

# Generates a dictionary of titles ('Sets') mapping to body content (long string of div.note-content)


def generate_title_dict(categories):
    """Generates a dictionary of dictionaries, mapping categories ('Data Science') to titles ('Sets') to content ('div.note-content')

    Args:
        categories (dict): The categories
    """
    category_title_dict = {}
    for category_name in categories:
        title_dict = {}
        for file in categories[category_name]:
            try:
                title = note_dict[file]['title']
                content = get_note_content(file)
                title_dict[title] = content
            except KeyError:
                print(
                    f"Failed to access title attribute of file {file}. Have you included this in the front-matter?")
        category_title_dict[category_name] = title_dict
    return category_title_dict


title_dict = generate_title_dict(categories)
