from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup

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

# Parsing the homepage and finding all the necessary tags
def parseHomepage(html):
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
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
                articles_data.append({
                    "title": title,
                    "datetime": date_time,
                    "tag": tag
                })
            else:
                print(f"Skipping article #{i}: Missing data")
        except Exception as e:
            print(f"Error parsing article #{i}: {e}")

    return articles_data
