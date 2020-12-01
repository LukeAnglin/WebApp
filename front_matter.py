import frontmatter
import pprint as pp
from itertools import chain
import os
import categories as cat
from frontmatter.default_handlers import YAMLHandler, TOMLHandler

pp.pprint(cat.category_dict)

# Create a new dictionary mapping filepaths to meta data from parsed markdown.
note_metadata = {}


def fetch_note_meta(filepath: str) -> dict:
    """Takes a filepath and returns a dictionary mapping the filepath to the metadata from a .md file.  Looks for the frontmatter in the .md file.  

    Args:
        filepath (str): The path of the file being parsed

    Returns:
        dict: A dictionary mapping the filepath to the metadata from a .md
    """
    with open(filepath) as file:
        note = frontmatter.load(file)
    return dict(note)


def generate_note_dict(category_dict: dict) -> dict:
    """Generates a dictionary of dictionaries mapping notes filepaths to their respective metadata

    Args:
        category (dict): A dictionary of the categories and their files/notes

    Returns:
        dict: A list of filepaths corresponding to the notes mapping to metadata 
    """
    # Store values of the dict in a list
    notes = list(category_dict.values())
    print(notes)
    # Flatten list
    notes = list(chain(*tuple(notes)))
    
    # Initialize empty list to hold dictionaries
    notes_meta = {}
    # Iterate through flattened list of notes.  Create a list of dictionaries mapping note
    for note in notes:
        # Remove the file extension
        note = os.path.splitext(note)[0]

        # Add '.md' extension
        note = note + '.md'

        # Fetch yaml data, and append the meta dictionary to the notes_meta dictionary
        notes_meta[note] = fetch_note_meta(note)

    # Return the dictionary of dictionaries
    return notes_meta


