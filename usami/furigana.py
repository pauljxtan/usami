import os
import sqlite3

from usami.settings import BASE_DIR

DB_PATH = os.path.join(BASE_DIR, "data", "jmdict-furigana.sqlite3")

# TODO
def get_furigana(kanji, furigana_delimiter=","):
    # with sqlite3.connect(DB_PATH) as conn:
    #     c = conn.cursor()
    #
    #     c.execute("SELECT furigana_split FROM kanji_furigana WHERE kanji = '?'", kanji)
    #     furigana = c.fetchone()[0]
    #
    #     furigana_delimited_elems = [""] * len(kanji)
    #     elems = furigana.split(";")
    #     for elem in elems:
    #         index, furigana = elem.split(":")
    #
    #     conn.commit()
    #     c.close()
    return








