import gzip
import os
import sqlite3

from usami.settings import BASE_DIR

def make_jmdictfurigana_db(source_path, db_path):
    with gzip.open(source_path, mode='rt', encoding="utf8") as infile:
        lines = infile.read().splitlines()

    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS kanji_furigana")
        c.execute("CREATE TABLE kanji_furigana (kanji TEXT, furigana TEXT, furigana_split TEXT)")

        lines = reversed(lines)
        for i, line in enumerate(lines):
            if i % 1000 == 0:
                print(i)
            kanji, furigana, furigana_split = line.split("|")
            c.execute("INSERT INTO kanji_furigana VALUES (?, ?, ?)", (kanji, furigana, furigana_split))

        conn.commit()
        c.close()

if __name__ == '__main__':
    source_path = os.path.join(BASE_DIR, "data", "JmdictFurigana.txt.gz")
    db_path = os.path.join(BASE_DIR, "data", "jmdict-furigana.sqlite3")
    make_jmdictfurigana_db(source_path, db_path)
