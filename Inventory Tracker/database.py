import sqlite3

conn = sqlite3.connect('inventory.db')

c = conn.cursor()

c.execute('''CREATE TABLE inventory
            ID text,
            name text,
            qty text''')


