import sqlite3

def create_tb(table):

    with sqlite3.connect(table) as conn:
        c = conn.cursor()
        


        c.execute('''
        CREATE TABLE books
        (name text, isbn text, qty real)
        ''')