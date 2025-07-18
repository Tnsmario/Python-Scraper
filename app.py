"""

Sources of inspiration:
https://www.youtube.com/watch?v=Xz514u4V_ts&t=235s
https://playwright.dev/python/docs/intro
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://www.chatgpt.com

"""
from flask import Flask, render_template, redirect, url_for
from scraper.fetcher import  fetchingHTML, parseHomepage
from database.db import  initDB, saveArticlesToDB, get_all_articles


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scrape")
def scrape():
    url = "https://www.hotnews.ro"
    html = fetchingHTML(url)
    articles = parseHomepage(html)

    if articles:
        initDB()
        saveArticlesToDB(articles)
    return redirect(url_for("articles"))


@app.route("/articles")
def articles():
    articles_list = get_all_articles()
    return render_template("articles.html", articles=articles_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)