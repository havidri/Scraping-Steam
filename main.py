import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/steam')
def top_sellers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    url = 'https://store.steampowered.com/games/#p=0&tab=TopSellers'
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    titles = soup.find_all('a', attrs={'class': 'tab_item'})

    return render_template('steam.html', titles=titles)


if __name__ == '__main__':
    app.run(debug=True)