from bs4 import BeautifulSoup
from urllib.parse import urljoin

links = ['https://www.thisamericanlife.org/blog/index.html','http://www.cnn.com/index.html','http://www.bbc.com/news/index.html','https://blogs.scientificamerican.com/index.html','https://en.wikipedia.org/wiki/Main_Page/index.html']

for i in range(5):
    fn = str(i)+'.html'
    with open(fn,'rb') as f:
        html = f.read()
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    pool = set()
    with open(str(11)+'.txt','w') as f:
        for aa in a:
            try:
                link = urljoin(links[i],aa['href'])
                if link not in pool:
                    f.write(link+'\n')
            except Exception as e:
                pass