#md5db.py
# -*- coding: utf-8 -*-

"""
@author Falko Benthin
@Date 27.12.2015
@brief database operations for schmuddelscriptsniper
"""

import sqlite3, os, time
# import logging

class md5db(object):
	#initialisieren
	def __init__(self):
		self.db = '/home/falko/muckyscriptsniper/md5sums.sqlite'
		#Datenbank verbinden
		#self.conn = sqlite3.connect(db, timeout=10)
		
	
	"""
	checks, if database contains an md5sum
	@param string md5sum
	@returns bool
	"""
	def getMD5(self, md5sum):
		#Datenbank verbinden
		conn = sqlite3.connect(self.db, timeout=10)
		cursor = conn.cursor()
		try:
		  	
			cursor.execute("SELECT id FROM md5sums WHERE md5sums = ?;", (md5sum,))
			data = cursor.fetchone()
		except sqlite3.OperationalError,e:
			time.sleep(3)
			print(str(e))
		conn.close()
		if data is None:
			return False
		else:
			return True

	def closeDB(self):
		pass
