#!/usr/bin/env python3.6

import sqlite3

conn = sqlite3.connect('vmfarms.db')

conn.execute('CREATE TABLE names (name TEXT)')

conn.close()
