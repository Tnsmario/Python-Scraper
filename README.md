# Python-Scraper

A **Flask** web application that automatically scrapes articles from the homepage of [HotNews.ro](https://www.hotnews.ro), stores them in a local database, and displays them through a simple web interface.

## How it works

1. The home page (`/`) shows a starting screen.
2. The `/scrape` route fetches the HTML from hotnews.ro (using Playwright), parses the homepage articles (using BeautifulSoup), and saves them to the database.
3. The `/articles` route displays the full list of saved articles, read back from the database.

## Tech stack

- **Python 3.11**
- **Flask** – web server and routing
- **Playwright** – HTML fetching/rendering (including dynamically loaded content)
- **BeautifulSoup4** – HTML parsing and data extraction
- **SQLite** (via the `database` module) – storage for scraped articles
- **Docker** – containerized deployment

## Project structure

```
Python-Scraper/
├── app.py                 # Flask entry point (routes: /, /scrape, /articles)
├── scraper/                # Scraping logic (fetching + HTML parsing)
├── database/                # Database logic (init, save, read articles)
├── templates/                # HTML templates (index, article list)
├── requirements.txt         # Python dependencies
├── Dockerfile                # Containerization config
└── .gitignore
```

## Local setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Tnsmario/Python-Scraper.git
   cd Python-Scraper
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   playwright install --with-deps
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open in your browser: [http://localhost:5000](http://localhost:5000)

## Running with Docker

```bash
docker build -t python-scraper .
docker run -p 5000:5000 python-scraper
```

The app will be available at [http://localhost:5000](http://localhost:5000).

## Usage

- Visit `/scrape` to trigger scraping of hotnews.ro's homepage articles and save them to the database.
- Visit `/articles` to view the list of saved articles.

## Background

This project was built as a learning exercise in Python web scraping, drawing on tutorials about Playwright, BeautifulSoup, and Flask.

## License

Not specified yet.
