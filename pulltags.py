#!/usr/bin/env python
# encoding: utf-8
"""
pulltags.py

Created by Eric Groo on 2010-02-08.
Copyright (c) 2010 __HomeGroo Tech__. All rights reserved.
"""
import sys
import os
from lxml import etree
import httplib2
import MySQLdb

conn = MySQLdb.connect (user = 'useextractor',
						passwd = 'extractor',
						db = 'gamerdb',
						use_unicode = True)
conn.autocommit(True)
cur = conn.cursor()
h = httplib2.Http('.cache')

def main():
	tagpointer = 1
	while True:
		a_url=u'http://www.360voice.com/api/leader.asp?type=1&start=%i' % tagpointer
		response, content = h.request(a_url)
		tree = etree.fromstring(content)
		gamers = tree[1].getchildren()
		if len(gamers)==0: break
		tagpointer+=len(gamers)
		maptags(gamers, cur)	
	
	conn.close()
	pass


def maptags(gamerlist, cur=cur):
	"""Takes a list of gamer nodes and passes appropriate tag data to mysql database"""
	for gamer in gamerlist:
		pid = gamer.findtext('id')
		tag = gamer.findtext('gamertag')
		rank = gamer.findtext('rank')
		country = gamer.findtext('country')
		cur.execute(
		""" INSERT INTO users (pid, tag, rank, country)
			VALUES (%s, %s, %s, %s)""", (pid, tag, rank, country)
			)
	pass

	
if __name__ == '__main__':
	main()