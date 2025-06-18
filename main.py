"""

Sources of inspiration:
https://www.youtube.com/watch?v=Xz514u4V_ts&t=235s
https://playwright.dev/python/docs/intro
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""
from scraper.fetcher import  fetchingHTML, parseHomepage
from database.db import  init_db, save_articles_to_db
import json

# Create the JSON file if it doesn't already exist
def saveToJSON(data, filename="articole.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data have been saved to {filename}")
    except Exception as e:
        print(f"Failed to save JSON: {e}")

if __name__ == "__main__":
    url = "https://www.hotnews.ro"
    print(f"Scraping {url} ...")

    html = fetchingHTML(url)
    articles = parseHomepage(html)

    if articles:
        saveToJSON(articles)
        init_db()
        save_articles_to_db(articles)
        print(f"Scraped {len(articles)} articles. Saved to 'articole.json'")
    else:
        print("Nu am gasit articole")
