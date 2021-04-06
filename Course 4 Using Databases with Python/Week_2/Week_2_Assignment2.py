# Week 2 Assignment 2
#
# Counting Organizations
#
# This application will read the mailbox data (mbox.txt) and 
# count the number of email messages per organization
# (i.e. domain name of the email address) using a database 
# with the following schema to maintain the counts.
#
# CREATE TABLE Counts (org TEXT, count INTEGER)
#
# When you have run the program on mbox.txt upload the 
# resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, 
# make sure to empty out the data before each run.
# The data file for this application is the same as in previous assignments: 
# http://www.py4e.com/code3/mbox.txt.

import sqlite3

conn = sqlite3.connect('countorg.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue

    pieces_space = line.split()
    email = pieces_space[1]

    pieces_at = email.split('@')
    org = pieces_at[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    # conn.commit()

conn.commit()


# https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
# sqlstr = 'SELECT org, count FROM Counts'
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()



