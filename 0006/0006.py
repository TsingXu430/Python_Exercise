from bs4 import BeautifulSoup
import io

with io.open('test.html',encoding='UTF-8') as file:
    html = file.read()
    soup = BeautifulSoup(html)
    listA = soup.find_all('a')
    listB = soup.find_all('link')
    listC = soup.find_all('img')

for a in listA:
    print(a['href'])
for b in listB:
    print(b['href'])
for c in listC:
    print(c['src'])