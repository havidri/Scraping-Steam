from uu import encode
import requests
from bs4 import BeautifulSoup
import csv

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
url = 'https://store.steampowered.com/games/#p=0&tab=NewReleases'

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')

new_releases = soup.findAll('a', attrs={'class': 'tab_item'})

file = open('data_result.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Price', 'Tags'])

for release in new_releases:
    if (release.find('div', attrs={'class': 'tab_item_name'}) != None):
        title = release.find('div', attrs={'class': 'tab_item_name'}).text
    else:
        title = ''

    if (release.find('div', attrs={'class': 'discount_final_price'}) != None):
        price = release.find('div', attrs={'class': 'discount_final_price'}).text
    else:
        price = ''

    if (release.find('div', attrs={'class': 'tab_item_top_tags'}) != None):
        tas = release.find('div', attrs={'class': 'tab_item_top_tags'}).text
    else:
        tas = ''

    file = open('data_result.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, price, tas])
    file.close()