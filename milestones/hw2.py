from bs4 import BeautifulSoup
import requests

r = requests.get('https://text.npr.org/')
html = r.text
soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all('a'):
    print(link)
