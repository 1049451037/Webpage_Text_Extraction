# Webpage_Text_Extraction

Extract main textual information from HTML.

## Requirement

* Python 3

## Installation

```shell
pip install pextract
```

## Example

```python
import requests
from bs4 import BeautifulSoup
import pextract as pe
from urllib.parse import urljoin

url = 'https://allaboutstevejobs.com/bio/short_bio'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
for img in soup.findAll('img'):
	img['src'] = urljoin(url, img['src'])
html, pval = pe.extract(soup, text_only = False, remove_img = False)
text, pval = pe.extract(soup)
print(pval) # This is a strong feature for web page classification
with open('out.html', 'w', encoding = 'utf-8') as f:
	f.write(html)
with open('out.txt', 'w', encoding = 'utf-8') as f:
	f.write(text)
```

