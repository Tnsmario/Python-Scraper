"""

Sources of inspiration:
https://www.youtube.com/watch?v=Xz514u4V_ts&t=235s
https://playwright.dev/python/docs/intro
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup
import json
import hashlib


# Open url using playwright
def fetchingHTML(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000)
            page_content = page.content()
            browser.close()
            return page_content
    except PlaywrightTimeout:
        print(f"Timeout while loading {url}")
        return None
    except Exception as e:
        print(f"Error during fetching: {e}")
        return None

def hash_logic(title, date, tag):
    key = f"{title.strip()}|{date.strip()}|{tag.strip()}"
    return hashlib.md5(key.encode("utf-8")).hexdigest()

# Parsing the homepage and finding all the necessary tags
def parseHomepage(html):
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')

    seen_hashes = set()
    articles_data = []

    containers = soup.select("article.post")

    # Searching the title, date & time and tag for each article

    for i, article in enumerate(containers, 1):
        try:
            title_tag = article.find(['h2'])
            title = title_tag.get_text(strip=True) if title_tag else None

            date_tag = article.find('time', class_='entry-date published')
            date_time = date_tag.get_text(strip=True) if date_tag else "N/A"

            tag_tag = article.find('div', class_='hn-category-tag')
            tag = tag_tag.get_text(strip=True) if tag_tag else "N/A"

            if title:
                article_hash = hash_logic(title, date_time, tag)
                if article_hash not in seen_hashes:
                    seen_hashes.add(article_hash)
                    articles_data.append({
                        "title": title,
                        "datetime": date_time,
                        "tag": tag
                    })
            else:
                print(f"Duplicate skipped (#{i})")
        except Exception as e:
            print(f"Error parsing article #{i}: {e}")

    return articles_data

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
    saveToJSON(articles)
    print(f"Scraped {len(articles)} articles. Saved to 'articole.json'")
