### will run script with concatenated URL
###Import Libraries
from bs4 import BeautifulSoup
import requests
from downloadfile import download_url
 


links = []
r = requests.get('https://samples.adsbexchange.com/readsb-hist/2022/05/01/')
html = r.text
soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all('a'):
    links.append(link.get('href'))

for link in links:
    if '.json.gz' in link:
        print('https://samples.adsbexchange.com/readsb-hist/2022/05/01/'+link)

datafile_path = '/Users/alexguay/Workspace/OperationRavenousSuckerPunch-2/data.txt'

download_url(datafile_path)



