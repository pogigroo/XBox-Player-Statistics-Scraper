#!/usr/bin/env python
# encoding: utf-8
"""
buildtables.py

Created by Eric Groo on 2010-02-10.
Copyright (c) 2010 __HomeGroo__. All rights reserved.
"""

import sys
import os
import MySQLdb
import csv

conn = MySQLdb.connect (user = 'useextractor',
						passwd = 'extractor',
						db = 'gamerdb',
						use_unicode = True)
conn.autocommit(True)

gamecursor = conn.cursor()
gamefile = "dat/games.csv"


def main():
	filereader = csv.reader(open(gamefile))
	for row in filereader:
		gamecursor.execute("""
			SELECT tag, min(entrydate) AS firstd 
			FROM history 
			WHERE match(body) AGAINST ('"%s"' IN BOOLEAN MODE) 
			GROUP BY tag""", (row[0]) ) 
		firstplayrows = cursor.fetchall()
		for firstplay in firstplayrows:
			print "%s, %s, %s" % (row[0], firstplay[0], firstplay[1])
	pass

if __name__ == '__main__':
	main()

