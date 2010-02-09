"""
pullprofiles.py

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

tagcursor = conn.cursor()
histcursor = conn.cursor()
h = httplib2.Http('.cache')

def main():
	for tag in gettags(tagcursor):
		a_url=u'http://www.360voice.com/api/blog-getentries.asp?tag=%s &played=1' % tag[0].rstrip()
		response, content = h.request(a_url)
		tree = etree.fromstring(content)
		tag = tree[0].findtext('gamertag')
		entrylist = tree[1].getchildren()
		mapentries(entrylist, histcursor, tag)	
	conn.close()
	print "Done"

def mapentries(entrylist, cur, tag):
	"""Takes a list of gamer nodes and passes appropriate tag data to mysql database"""
	for entry in entrylist:
		blogid = entry.findtext('blogid')
		body = entry.findtext('body')
		entrydate = formatdate(entry.findtext('entrydate'))
		try:
			cur.execute(
			""" INSERT INTO history (blogid, tag, entrydate, body)
				VALUES (%s, %s, %s, %s)""", (blogid, tag, entrydate, body)
				)
		except MySQLdb.Error, e:
			print "Error %d: %s, blogid: %s" % (e.args[0], e.args[1], blogid)
	pass
	
def gettags(tagcursor):
	"""Generator supllying tags from database"""
	tagcursor.execute(""" SELECT tag FROM users """)
	row = tagcursor.fetchone()
	while row != None:
		yield row[0]
		row = tagcursor.fetchone()
	else:
		return

def formatdate(datestring):
	"""Changes d/m/yyyy date string to YYYY-MM-DD format"""
	day, month, year = datestring.split('/', 3)
	newdatestring = year + "-" + month.rjust(2, '0') + "-" + day.rjust(2, '0')
	return newdatestring
	
if __name__ == '__main__':
	main()