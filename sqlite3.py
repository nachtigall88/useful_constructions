import sqlite as sq

"""код для створення бази даних"""
with sq.connect('word_data.db') as con:
      cur = con.cursor()
      cur.execute("""CREATE TABLE IF NOT EXIST words (
      art TEXT,
      word TEXT,
      translation TEXT
      )""")

"""код для додавання даних у базу"""
with sq.connect('word_data.db') as con:
      cur = con.cursor()
      cur.execute(f"""INSERT INTO words VALUES (
      '{data.art}', '{data.word}', '{data.translation}'
      )""")
