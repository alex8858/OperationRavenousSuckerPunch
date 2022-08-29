import os.path
import requests

if __name__ == "__main__":
    url='https://samples.adsbexchange.com/readsb-hist/2022/05/01/235745Z.json.gz'

    def download_url(url):
        filename= os.path.basename(url)
        r = requests.get(url, allow_redirects=True)
        open('data/' + filename, 'wb').write(r.content)

    download_url(url)
