import requests
from bs4 import BeautifulSoup

from itertools import product
from string import ascii_lowercase

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]
print (keywords)


url = 'https://satoshistreasure.xyz/'

def findandsave(l):
    r = requests.get(f'{url}{l}')
    soup = BeautifulSoup(r.content)
    found = soup.find('h1')
    if found and 'Not Found' in found:
        print('skip')
    else:
        file = open('static/'+l+'.html', "w")
        file.write(soup.prettify())
        file.close()

for w in keywords:
    findandsave(w)
# for i in range(4):
#     findandsave(str(i))
#     