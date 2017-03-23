from bs4 import BeautifulSoup
from urllib.parse import urljoin

links = ['http://www.bbc.com/news/index.html']

fn = 'bbc.html'
with open(fn,'rb') as f:
    html = f.read()
soup = BeautifulSoup(html,'html.parser')
a = soup.find_all('a')
pool = set()
with open('bbc.txt','w') as f:
    for aa in a:
        try:
            link = urljoin(links[0],aa['href'])
            if link not in pool:
                f.write(link+'\n')
        except Exception as e:
            pass