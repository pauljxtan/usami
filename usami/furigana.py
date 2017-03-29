import os
import sqlite3

from usami.settings import BASE_DIR

DB_PATH = os.path.join(BASE_DIR, "data", "jmdict-furigana.sqlite3")

def get_furigana(kanji, furigana_delimiter=","):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()

        # Binding not working properly for some reason
        #c.execute("SELECT furigana_split FROM kanji_furigana WHERE kanji = ?", kanji)
        sql = "SELECT furigana_split FROM kanji_furigana WHERE kanji = '{}'".format(kanji)
        print(sql)
        c.execute(sql)
        results = c.fetchall()
        print(results)
        all_furigana = [result[0] for result in results]

        c.close()

    all_furigana_delimited = []

    for furigana in all_furigana:
        furigana_delimited_elems = [""] * len(kanji)
        elems = furigana.split(";")
        for elem in elems:
            index, furi = elem.split(":")
            try:
                i = int(index)
                furigana_delimited_elems[i] = furi
            except ValueError:
                i, j = index.split("-")
                for k in range(i, j + 1):
                    furigana_delimited_elems[k] = furi[k - i]

        all_furigana_delimited.append(furigana_delimiter.join(furigana_delimited_elems))

    return all_furigana_delimited

if __name__ == '__main__':
    print(get_furigana("恵"))






