import os.path
import pprint as pp
import sys

# The purpose of this file is to add the relevant categories and create a dictionary full of the category mapping to the relevant files.

# Edit the following lines, 8-13, in order to update some of the features.

# Remove certain folders that I don't want
names_to_remove = ['MLProjects', '.ipynb_checkpoints']

# Change the names_to_change and new_name arrays to update
names_to_change = ['JS']
new_names = ['JavaScript']

# CODE FOR THIS

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
    category_dict['Machine Learning'] = ml_notes
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
        del categories[name]

    return categories

# Create the categories
create_categories()

# Pass categories to modify_categories to be fixed
categories = modify_categories(category_dict)

