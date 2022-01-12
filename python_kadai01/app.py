import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""      
# **** ここを実装します（基礎課題） ****

# 1. はてブのホットエントリーページのHTMLを取得する
    with urlopen("https://news.yahoo.co.jp") as res:
        html = res.read().decode("utf-8")

# 2. BeautifulSoupでHTMLを読み込む
    soup = BeautifulSoup(html, "html.parser")

# 3. 記事一覧を取得する class="sc-frDJqD bJCuGd"
    news = soup.select(".bJCuGd")
    # titles = [t.string for t in titles]
# 4. ランダムに1件取得する
    shuffle(news)
    item = news[0]
    pprint(item)
    return json.dumps({
        "content" : item.text,
        "link": item.get('href')
    })

# @app.route("/api/information")
# def api_information():
#     """
#         **** ここを実装します（発展課題） ****
#         ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
#         ・お天気APIなども良いかも
#         ・関数名は適宜変更してください
#     """
#     pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)