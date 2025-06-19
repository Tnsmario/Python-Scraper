import sqlite3

def initDB(db_name="articole.db"):
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

def saveArticlesToDB(articles, db_name="articole.db"):
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


def get_all_articles(db_name="articole.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT title, datetime, tag FROM articole ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()

    # Transforming into dictionaries list
    return [{"title": r[0], "datetime": r[1], "tag": r[2]} for r in rows]