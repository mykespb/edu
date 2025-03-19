#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-28 2025-03-19 1.9
# sql-simple.py

# ~ Simple work with sqlite3 database in memory.

# ~ import os
import sqlite3 as sql

#db = '/tmp/one.db'
db = ":memory:"

print("\nHello! Let's play with database.\n")

# make connection
conn = sql.connect(db)
cur = conn.cursor()

# make calcuilations

cur.execute("SELECT 2*2")
result = cur.fetchone()[0]
print(f"{result=}")

# get current date
cur.execute("SELECT date()")
today = cur.fetchone()[0]
print(f"{today=}")

cur.execute("SELECT date()")
today = cur.fetchall()[0][0]
print(f"{today=}")

# create 1 table
print('\nCreate') 
cmd = "CREATE TABLE people (first, last, bd)"
#cmd = "CREATE TABLE IF NOT EXISTS people (first, last, bd)"
#cmd = "CREATE TABLE IF NOT EXISTS people (first TEXT, last TEXT, bd TEXT)"
conn.execute(cmd)
conn.commit()

# populate it with data

print('\nPopulate')
cur.execute("INSERT INTO people (first, last, bd) VALUES (?, ?, ?)",
    ("Some", "Body", "1999-12-31"))
conn.commit()

# read all data and print them

print('\nRead') 
cmd = "SELECT * FROM people"
data = cur.execute(cmd)

print('\nAll data:')
for row in data:
    print(row)

# populate many

persons = [
    ("John", "Done", "2010-01-21"),
    ("Mike", "Soft", "2012-02-11"),
    ("Mike", "Hard", "2015-03-01"),
    ("Dennis", "Sooner", "2008-05-31"),
    ]

cur.executemany("INSERT INTO people (first, last, bd) VALUES (?, ?, ?)", persons)
conn.commit()

# read all data and print them

cmd = "SELECT * FROM people"
data = cur.execute(cmd)

print('\nAll data:')
for row in data:
    print(row)
    
# read selected data    

data = cur.execute("SELECT bd, last FROM people WHERE bd > '2009' ORDER BY bd DESC ")

# print them
print('\nSelected data with descending birthdays:')
for row in data:
    print(row)

# update db

print('\nUpdate') 
cur.execute("UPDATE people SET bd = '2000-01-01' WHERE last = 'Soft' ")
conn.commit()

# read all data and print them

cmd = "SELECT * FROM people"
data = cur.execute(cmd)
print('\nAll data:')
for row in data:
    print(row)

# delete data

print('\nDelete') 
cur.execute("DELETE FROM people WHERE last = 'Sooner' ")
conn.commit()

# read all data and print them

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

# ~ result=4
# ~ today='2025-03-19'
# ~ today='2025-03-19'

# ~ Create

# ~ Populate

# ~ Read

# ~ All data:
# ~ ('Some', 'Body', '1999-12-31')

# ~ All data:
# ~ ('Some', 'Body', '1999-12-31')
# ~ ('John', 'Done', '2010-01-21')
# ~ ('Mike', 'Soft', '2012-02-11')
# ~ ('Mike', 'Hard', '2015-03-01')
# ~ ('Dennis', 'Sooner', '2008-05-31')

# ~ Selected data:
# ~ ('2015-03-01', 'Hard')
# ~ ('2012-02-11', 'Soft')
# ~ ('2010-01-21', 'Done')

# ~ Update

# ~ All data:
# ~ ('Some', 'Body', '1999-12-31')
# ~ ('John', 'Done', '2010-01-21')
# ~ ('Mike', 'Soft', '2000-01-01')
# ~ ('Mike', 'Hard', '2015-03-01')
# ~ ('Dennis', 'Sooner', '2008-05-31')

# ~ Delete

# ~ All data:
# ~ ('Some', 'Body', '1999-12-31')
# ~ ('John', 'Done', '2010-01-21')
# ~ ('Mike', 'Soft', '2000-01-01')
# ~ ('Mike', 'Hard', '2015-03-01')

# ~ DB is closed. No reading or writing is possible now.
# ~ Good-bye!
