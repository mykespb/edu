#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-28 2025-03-05 1.2
# sql-simple.py

# ~ Simple work with sqlite3 database in memory.

# ~ import os
import sqlite3 as sql

#db = '/tmp/one.db'
db = ":memory:"

print("Hello! Let's play with database.")

# make connection
conn = sql.connect(db)
cur = conn.cursor()

# get current date
cur.execute("SELECT date()")
today = cur.fetchall()[0][0]
print(f"{today=}")

# create 1 table
cmd = "CREATE TABLE IF NOT EXISTS people (first TEXT, last TEXT, bd TEXT)"
conn.execute(cmd)
conn.commit()

# populate it with data
persons = [
    ("John", "Done", "2010-01-21"),
    ("Mike", "Soft", "2012-02-11"),
    ("Dennis", "Sooner", "2008-05-31"),
    ]

cur.executemany("INSERT INTO people (first, last, bd) VALUES (?, ?, ?)", persons)
conn.commit()

# read all data
cmd = "SELECT * FROM people"
data = cur.execute(cmd)

# print them
print('\nAll data:')
for row in data:
    print(row)
    
# read selected data    

data = cur.execute("SELECT bd, last FROM people WHERE bd > '2009' ORDER BY bd DESC ")

# print them
print('\nSelected data:')
for row in data:
    print(row)

cur.close()
conn.close()

print("\nDB is closed. No reading or writing is possible now.\nGood-bye!")


# --- results: ---

# ~ Hello! Let's play with database.
# ~ today='2025-03-05'

# ~ All data:
# ~ ('John', 'Done', '2010-01-21')
# ~ ('Mike', 'Soft', '2012-02-11')
# ~ ('Dennis', 'Sooner', '2008-05-31')

# ~ Selected data:
# ~ ('2012-02-11', 'Soft')
# ~ ('2010-01-21', 'Done')

# ~ DB is closed. No reading or writing is possible now.
# ~ Good-bye!
