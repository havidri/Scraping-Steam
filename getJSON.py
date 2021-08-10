import requests, json

url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'

params = {
    'appid':'440',
    'count':'3',
    'maxlength':'300',
    'format':'json'
}

req = requests.get(url, params=params).json()

users = req['appnews']['newsitems']

for user in users:
    print(user['appid'])
    print(user['title'])
    print(user['url'])