import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

url = 'https://store.steampowered.com/games/#p=0&tab=TopSellers'
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')

titles = soup.find_all('a', attrs={'class': 'tab_item'})

# print(titles)

for top_seller in titles:
    print('Title: ', top_seller.find('div', attrs={'class': 'tab_item_name'}).text)
    print('Image Game: ', top_seller.find('div', attrs={'class': 'tab_item_cap'}).find('img'))

