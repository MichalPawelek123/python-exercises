"""
Use the BeautifulSoup and requests Python packages to print out a list of all the
article titles on the New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup


url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup_nyt = BeautifulSoup(r_html, 'html.parser')
articles = soup_nyt.find_all('p', class_="indicate-hover")

titles = [title.get_text() for title in articles]

for title in titles: 
    print(title)
