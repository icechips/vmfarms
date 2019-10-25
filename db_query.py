#!/usr/bin/env python3.6

import sqlite3

conn = sqlite3.connect('vmfarms.db')

result = conn.execute("SELECT * from NAMES")

for row in result:
    print("NAME = ", row[0])

conn.close()    
