#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-28 2025-03-17 1.4
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
print('\nCreate') 
cmd = "CREATE TABLE IF NOT EXISTS people (first TEXT, last TEXT, bd TEXT)"
conn.execute(cmd)
conn.commit()

# populate it with data

print('\nPopulate') 
persons = [
    ("John", "Done", "2010-01-21"),
    ("Mike", "Soft", "2012-02-11"),
    ("Dennis", "Sooner", "2008-05-31"),
    ]

cur.executemany("INSERT INTO people (first, last, bd) VALUES (?, ?, ?)", persons)
conn.commit()

# read all data
print('\nRead') 
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

# update db

print('\nUpdate') 
cur.execute("UPDATE people SET bd = '2000-01-01' WHERE last = 'Soft' ")
conn.commit()

# read all data
cmd = "SELECT * FROM people"
data = cur.execute(cmd)
print('\nAll data:')
for row in data:
    print(row)

# delete data

print('\nDelete') 
cur.execute("DELETE FROM people WHERE last = 'Sooner' ")
conn.commit()

# read all data
cmd = "SELECT * FROM people"
data = cur.execute(cmd)
print('\nAll data:')
for row in data:
    print(row)

# close all

cur.close()
conn.close()

print("\nDB is closed. No reading or writing is possible now.\nGood-bye!\n")


# --- results: ---

# ~ Hello! Let's play with database.
# ~ today='2025-03-17'

# ~ Create

# ~ Populate

# ~ Read

# ~ All data:
# ~ ('John', 'Done', '2010-01-21')
# ~ ('Mike', 'Soft', '2012-02-11')
# ~ ('Dennis', 'Sooner', '2008-05-31')

# ~ Selected data:
# ~ ('2012-02-11', 'Soft')
# ~ ('2010-01-21', 'Done')

# ~ Update

# ~ All data:
# ~ ('John', 'Done', '2010-01-21')
# ~ ('Mike', 'Soft', '2000-01-01')
# ~ ('Dennis', 'Sooner', '2008-05-31')

# ~ Delete

# ~ All data:
# ~ ('John', 'Done', '2010-01-21')
# ~ ('Mike', 'Soft', '2000-01-01')

# ~ DB is closed. No reading or writing is possible now.
# ~ Good-bye!
