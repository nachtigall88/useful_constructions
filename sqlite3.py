import sqlite as sq

with sq.connect('word_data.db') as con:
      cur = con.cursor()
      cur.execute("""CREATE TABLE IF NOT EXIST words (
      art TEXT,
      word TEXT,
      translation TEXT
)""")
