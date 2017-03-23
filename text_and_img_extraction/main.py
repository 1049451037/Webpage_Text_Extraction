# coding : utf-8

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

global v
global L


def has_style(tag):
    return tag.has_attr('style')


def has_class(tag):
    return tag.has_attr('class')


def dfs(soup):
    if soup.name == 'a' or soup.name == 'br':
        return
    try:
        ls = len(str(soup))
        img = soup.find_all('img')
        im = 0
        timg = 0
        for j in img:
            im += len(j)
            timg += len(j.get_text())
        ls -= im
        lt = len(soup.get_text()) - timg
        a = soup.find_all('a')
        at = 0
        for j in a:
            at += len(j.get_text())
        lvt = lt - at
        v.append((soup, lt / ls * lvt))
        for child in soup.children:
            dfs(child)
    except Exception as e:
        pass


def clean(soup):
    if soup.name == 'br':
        return
    try:
        ll = 0
        for j in soup.strings:
            ll += len(j.replace('\n', ''))
        if ll == 0:
            soup.decompose()
        else:
            for child in soup.children:
                clean(child)
    except Exception as e:
        pass

os.makedirs('output',exist_ok=True)
file = open("out.csv", "w")
file.close()
with open('encoding.txt', 'r') as f:
    page_encoding = f.readline().replace('\n', '')
    file_encoding = f.readline().replace('\n', '')
pool = set()
with open("pool.txt", "r") as f:
    for link in f.readlines():
        s = link.replace('\n', '')
        if s != '' and s not in pool:
            pool.add(s)
cnt = 0
for url in pool:
    try:
        v = []
        par = urlparse(url)
        Default_Header = {'X-Requested-With': 'XMLHttpRequest',
                          'Referer': par[0] + '://' + par[1],
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
                          'Host': par[1]}
        r = requests.get(url, headers=Default_Header, timeout=10).content
        soup = BeautifulSoup(r, 'html.parser', from_encoding=page_encoding)  # encoding should be chosen properly
        title = ''
        try:
            title = soup.title.string
        except Exception as e:
            pass
        filt = ['script', 'noscript', 'style', 'embed', 'label', 'form', 'input', 'iframe', 'head', 'meta', 'link',
                'object', 'aside', 'channel']
        for ff in filt:
            for i in soup.find_all(ff):
                i.decompose()
        for tag in soup.find_all(has_style):
            del tag['style']
        for tag in soup.find_all(has_class):
            del tag['class']
        clean(soup)
        LVT = len(soup.get_text())
        for i in soup.find_all('a'):
            LVT -= len(i.get_text())
        dfs(soup)
        mij = 0
        for i in range(len(v)):
            if v[i][1] > v[mij][1]:
                mij = i
        print(cnt, mij, v[mij][1] / LVT)
        file = open("out.csv", "a")
        file.write("%d,%d,%f\n" % (cnt, mij, v[mij][1] / LVT))
        file.close()
        with open("output/out" + str(cnt) + ".html", "w",
                  encoding=file_encoding) as f:  # encoding should be chosen properly
            f.write(
                "<a href='out" + str(cnt - 1) + ".html'>pre</a> <a href='out" + str(
                    cnt + 1) + ".html'>next</a>\n<h3>initial url: </h3><a href=\"" + url + "\"target='_blank'>" + url + "</a><br><h3>textual infomation: </h3><h4>" + title + "</h4>\n")
            f.write(str(v[mij][0]))
        with open("output/out" + str(cnt) + ".txt", "w",
                  encoding=file_encoding) as f:  # encoding should be chosen properly
            f.write(title + '\n')
            tsoup = BeautifulSoup(v[mij][0].prettify(), 'html.parser')
            for img in tsoup.find_all('img'):
                img.decompose()
            ss = tsoup.get_text()
            s = ss.split('\n')
            for line in s:
                if line != '':
                    f.write(line + '\n')
        cnt += 1
    except Exception as e:
        print(e)
input()
