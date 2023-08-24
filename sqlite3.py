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

def check_if_exists(data):
  """метод перевіряє, чи є слово, що додається, в базі"""
  flag = True
  with sq.connect('database.db') as con:
      cur = con.cursor()
      cur.execute("""SELECT * FROM table""")
      result = cur.fetchall()
      for i in result:
          if data in i:
              flag = False
  return flag








