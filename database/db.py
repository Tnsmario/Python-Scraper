import sqlite3

def init_db(db_name="articole.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articole (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            datetime TEXT,
            tag TEXT
            )
     ''')
    conn.commit()
    conn.close()

def save_articles_to_db(articles, db_name="articole.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for article in articles:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO articole (title, datetime, tag)
                VALUES (?, ?, ?)
             ''',(article['title'], article['datetime'], article['tag']))
        except Exception as e:
            print(f"Eroare la inserarea articolului: {e}")

    conn.commit()
    conn.close()
    print(f"Am salvat articolele in baza de date {db_name}")