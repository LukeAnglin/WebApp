import os
import sys

categories = os.listdir('categories')
# Remove .DS_Store
categories = categories[1:]

print(categories)
