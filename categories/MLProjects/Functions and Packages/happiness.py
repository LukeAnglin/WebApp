import os
import requests

#download vars
DOWNLOAD_URL = "https://www.kaggle.com/unsdsn/world-happiness?select=2019.csv"
happiness_file = os.path.join("..", "data", "happiness.csv")


def download_file(url, filename):
    ''' Downloads file from the url and save it as filename '''
    # check if file already exists
    if not os.path.isfile(filename):
        print('Downloading File')
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(filename, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
    else:
        print('File exists')

download_file(DOWNLOAD_URL, happiness_file)