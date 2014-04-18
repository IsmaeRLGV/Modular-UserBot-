#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
	import cPickle as pickle
except ImportError:
	import pickle

class db:
	def __init__(self, filename, i=None):
		self.filename=filename
	def open_db(self):
		try:
			fichero = file("%s.dat" % self.filename )
			fichero = pickle.load(fichero)
			return fichero
		except (IOError,EOFError):
			pass
	def create_db(self):
		fichero = file("%s.dat" % self.filename, "w")
		fichero.close()
		
class database:
	def __init__(self,filename,i):
		self.filename=filename
		self.i=i
	def W_db(self):
		fichero = file("%s.dat" % self.filename, "w")
		pickle.dump(self.i, fichero)
		fichero.close()
	def a_db(self):
		fichero = file("%s.dat" % self.filename, "a")
		pickle.dump(self.i, fichero)
		fichero.close()
