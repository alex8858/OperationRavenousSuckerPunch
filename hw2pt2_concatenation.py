### will run script with concatenated URL
###Import Libraries
from bs4 import BeautifulSoup
import requests

###Create .txt file

f = open("Data.txt","w+", encoding='utf-8', newline='') 


links = []
r = requests.get('https://samples.adsbexchange.com/readsb-hist/2022/05/01/')
html = r.text
soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all('a'):
    links.append(link.get('href'))

for link in links:
    print('https://samples.adsbexchange.com/readsb-hist/2022/05/01/'+link)

print(len(links))

f.write('https://samples.adsbexchange.com/readsb-hist/2022/05/01/'+link)

f.close()


