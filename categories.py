import os
import sys

# Categories are in the 'categories' folder in the root directory of the project
categories = os.listdir('categories')
# Remove .DS_Store
categories = categories[1:]

# Set the initial categories directory
categories_dir = '/categories'

for category in categories:
    category_dir = os.path.join(categories_dir, category)
    print(category_dir)
