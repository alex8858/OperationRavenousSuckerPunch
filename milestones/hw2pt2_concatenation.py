### will run script with concatenated URL

###Need to still make it into a .txt file


from bs4 import BeautifulSoup
import requests

links = []
r = requests.get('https://samples.adsbexchange.com/readsb-hist/2022/05/01/')
html = r.text
soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all('a'):
    links.append(link.get('href'))

for link in links:
    print('https://samples.adsbexchange.com/readsb-hist/2022/05/01/'+link)

print(len(links))





