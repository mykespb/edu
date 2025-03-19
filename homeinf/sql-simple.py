#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-28 2025-03-19 1.12
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
print('\n=== Create ===') 
cmd = "CREATE TABLE people (first, last, bd)"
#cmd = "CREATE TABLE IF NOT EXISTS people (first, last, bd)"
#cmd = "CREATE TABLE IF NOT EXISTS people (first TEXT, last TEXT, bd TEXT)"
conn.execute(cmd)
conn.commit()

print('\nOk')

# populate it with data

print('\n=== Populate ===')
cur.execute("INSERT INTO people (first, last, bd) VALUES (?, ?, ?)",
    ("Some", "Body", "1999-12-31"))
conn.commit()

print('\nOk')

# read all data and print them

print('\n=== Read ===') 
cmd = "SELECT rowid, * FROM people"
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

cmd = "SELECT rowid, * FROM people"
data = cur.execute(cmd)

print('\nAll data:')
for row in data:
    print(row)
    
# read selected data    

data = cur.execute("SELECT rowid, bd, last FROM people WHERE bd > '2009' ORDER BY bd DESC ")

# ~ print(dir(data))
# print them
print(f'\nSelected data with descending birthdays:')
num = 0
for row in data:
    print(row)
    num += 1
print(f"Found {num} record(s).")

# read selected data, who has birthday this month

cur.execute("SELECT date()")
today = cur.fetchone()[0]
month = today[5:7]

print(f"\nLook for persons of current {month=}")

data = cur.execute("SELECT rowid, * FROM people WHERE substr(bd, 6, 2) = ? ORDER BY bd ASC ", (month,))

# print them
print('\nSelected data with ascending birthdays:')
num = 0
for row in data:
    print(row)
    num += 1
print(f"Found {num} record(s).")

# update db

print('\n=== Update ===') 
cur.execute("UPDATE people SET bd = '2000-01-01' WHERE last = 'Soft' ")
conn.commit()

# read all data and print them

cmd = "SELECT rowid, * FROM people"
data = cur.execute(cmd)
print('\nAll data:')
for row in data:
    print(row)

# delete data

print('\n=== Delete ===') 
cur.execute("DELETE FROM people WHERE last = 'Done' ")
conn.commit()

# read all data and print them

cmd = "SELECT rowid, * FROM people"
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

# ~ === Create ===

# ~ Ok

# ~ === Populate ===

# ~ Ok

# ~ === Read ===

# ~ All data:
# ~ (1, 'Some', 'Body', '1999-12-31')

# ~ All data:
# ~ (1, 'Some', 'Body', '1999-12-31')
# ~ (2, 'John', 'Done', '2010-01-21')
# ~ (3, 'Mike', 'Soft', '2012-02-11')
# ~ (4, 'Mike', 'Hard', '2015-03-01')
# ~ (5, 'Dennis', 'Sooner', '2008-05-31')

# ~ Selected data with descending birthdays:
# ~ (4, '2015-03-01', 'Hard')
# ~ (3, '2012-02-11', 'Soft')
# ~ (2, '2010-01-21', 'Done')
# ~ Found 3 record(s).

# ~ Look for persons of current month='03'

# ~ Selected data with ascending birthdays:
# ~ (4, 'Mike', 'Hard', '2015-03-01')
# ~ Found 1 record(s).

# ~ === Update ===

# ~ All data:
# ~ (1, 'Some', 'Body', '1999-12-31')
# ~ (2, 'John', 'Done', '2010-01-21')
# ~ (3, 'Mike', 'Soft', '2000-01-01')
# ~ (4, 'Mike', 'Hard', '2015-03-01')
# ~ (5, 'Dennis', 'Sooner', '2008-05-31')

# ~ === Delete ===

# ~ All data:
# ~ (1, 'Some', 'Body', '1999-12-31')
# ~ (3, 'Mike', 'Soft', '2000-01-01')
# ~ (4, 'Mike', 'Hard', '2015-03-01')
# ~ (5, 'Dennis', 'Sooner', '2008-05-31')

# ~ DB is closed. No reading or writing is possible now.
# ~ Good-bye!
