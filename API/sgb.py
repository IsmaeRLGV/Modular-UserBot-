#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arrays,privs
class conv_type:
	def __init__(self, i):
		self.i=i
	def conv_int(self):
		try:
			conv=int(self.i)
			return conv
		except ValueError:
			pass
	def conv_str(self):
		a=[]
		b=()
		c=int(0)
		if type(self.i) == type(a):
			conv = " ".join(self.i)
			return conv
		if type(self.i) == type(b):
			conv = " ".join(self.i)
			return conv
		if type(self.i) == type(c):
			return "%s" % self.i
class game:
	def __init__(self, user,i=None):
		self.user=user
		self.j=privs.IsRegister(self.user)
		self.i=i
	def	PtsOfUser(self):
		if self.j[0]:
			return (self.j[1],arrays.DB_user[self.j[1]][3])
	
	def update_acount(self):
		if self.j[0]:
			if self.i.find("+")!=-1:
				arrays.DB_user[self.j[1]][3]+=int(self.i.split("+")[1])
			elif self.i.find("-")!=-1:
				arrays.DB_user[self.j[1]][3]+=int(self.i.split("-")[1])		
	
def top():
	cList=arrays.DB_user
	for i in range(1, len(cList)):
		for j in range(0, len(cList)-i):
			if cList[j][3] > cList[j+1][3]:
				elemento=cList[j]
				cList[j]=cList[j+1]
				cList[j+1]=elemento
	
	cList.reverse()
	return cList
