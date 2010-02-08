import MySQLdb

conn = MySQLdb.connect (user = 'useextractor',
						passwd = 'extractor',
						db = 'gamerdb',
						use_unicode = True)

# TODO - CONVERT mM/dD/YYYY to YYYY-MM-DD format!!!