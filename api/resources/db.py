import sqlite3

import advertisements

class Db:
  def __init__(self):
    self.conn = sqlite3.connect('crowd.db')
    self.init()

  def init(self):
    c = self.conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS advertisements (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      resource_url TEXT NOT NULL,
      type CHAR(15) NOT NULL
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS reactions (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      ad_id INTEGER NOT NULL
    )''')

    self.conn.commit()

  def get_advertisements(self):
    c = self.conn.cursor()
    res = c.execute('''SELECT * FROM advertisements''')

    ads = []
    for row in res:
      ad = advertisements.Advertisement.from_json({
        'id': row[0],
        'title': row[1],
        'resource_url': row[2],
        'type': row[3]
      })
      ads.append(ad)
    return ads

  def add_advertisement(self, ad):
    c = self.conn.cursor()

    c.execute(
      'INSERT INTO advertisements VALUES (NULL, ?, ?, ?)',
      (ad.title, ad.resource_url, ad.type)
    )

    self.conn.commit()

    ad.id = c.lastrowid
    return ad 

