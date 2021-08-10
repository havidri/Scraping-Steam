import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

url = 'https://store.steampowered.com/games/#p=0&tab=TopSellers'
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')

images = soup.find_all('a', attrs={'class': 'tab_item'})

for img in images:
    imageUrl = img.find('img', attrs={'class': 'tab_item_cap_img'})['src']
    titles = img.find('div', attrs={'class': 'tab_item_name'}).text
    res = requests.get(imageUrl, headers=headers, stream=True)
    fileName = imageUrl.split('/')[-1].split('?')[0]
    ext = fileName[-4:]
    if res.ok:
        with open('images/' + re.sub(r'(?u)[^-\w.]', '_', titles) + ext, 'wb') as a:
            a.write(res.content)
