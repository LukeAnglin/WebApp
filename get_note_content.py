import requests
from bs4 import BeautifulSoup


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
        return "Failed to find file"

