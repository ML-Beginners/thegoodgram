from typing import List, Any

import requests
import urllib.request
from bs4 import BeautifulSoup
import json
import os
import cv2

# Url of the page source
url = 'http://www.ecoindia.com/flora/trees/'

# Got the source code.
page = requests.get(url)

# BeautifulSoup Class
soup = BeautifulSoup(page.content, 'html.parser')

# Total 9 tables are there on the webpage
tree_html = soup.find_all('td', valign="TOP", class_='')

# Considering first 20
tree_td = tree_html[:20]
trees = tree_html[:6]

# Initializing empty lists
name = []
image = []
about = []

# Iterating over every tree
for tree in tree_td:
    # Getting names
    name.append(tree.find('a').get_text())

    # Downloading image
    IMG_URL = tree.find_all('img', align="MIDDLE")[0].get('src')
    IMG_PATH = os.path.basename(IMG_URL)
    urllib.request.urlretrieve(IMG_URL, IMG_PATH)

    # Getting pixels
    image.append(cv2.cvtColor(cv2.imread(IMG_PATH), cv2.COLOR_BGR2RGB).tolist())

    # Deleting the image
    os.remove(IMG_PATH)

    # About each trees
    about.append(tree.find('div', align='JUSTIFY', class_="text-tbl").get_text())

# Creating the dictionary
trees = dict(name=name, image=image, about=about)

# Creating a file from it
with open('trees.csv', 'a') as file:
    json.dump(trees, file)
