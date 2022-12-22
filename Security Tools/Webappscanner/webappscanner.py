import requests
from bs4 import BeautifulSoup

# URL of the web application to be scanned.
url = "http://example.com/"

# a GET request is sent to the URL.
response = requests.get(url)

# The HTML of the page is obtained.
html = response.text

# The HTML is parsed using the Beautiful Soup library.
soup = BeautifulSoup(html, 'html.parser')

# Find all links in the HTML.
links = soup.find_all('a')

# Scrolls through each link and displays its URL.
for link in links:
    print(link.get('href'))
