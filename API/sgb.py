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

def top(self):
	rst=[]
	q=game('PTS', self.list).pts_ls()
	for i in q:
		ii=conv_type(i).conv_int()
		rst.append(ii)
	for i in range(1, len(rst)):
		for j in range(0, len(rst)-i):
			if rst[j[0]] > rst[j+1[0]]:
				elemento=rst[j]
				rst[j]=rst[j+1]
				rst[j+1]=elemento
	return rst			
	
def i():
	for i in range(1, len(lista)):
		if lista[j][0] > lista[j+1][0]:
			elemento=lista[j]
			lista[j]=lista[j+1]
			lista[j+1]=elemento
