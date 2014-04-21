#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arrays,re,db,client
def IsRegister(user):
	try:
		InDB=re.compile(r'%s' % user, re.IGNORECASE)
	except sre_constants.error:
		InDB=re.compile(r'Fgt5dR5s333', re.IGNORECASE)
	isRegister=False
	while isRegister == False:
		for i in arrays.DB_user:
			if InDB.match(i[0][0]):
				posc=arrays.DB_user.index(i)
				isRegister=True
		break		
	if isRegister == True:
		return [True, posc]
	elif isRegister == False:
		return (False,0)
		
def info(int,user):
	"""Muestra la informacion del usuario especificado.
	   1 - Para la informacion del status.
	   2 - Para mostrar la contraseña.
	   3 - Para mostrar el host.
	   4 - Para mostrar los flags.
	   5 - Para mostrar los puntos de juego.
	   0 - Toda la informacion."""
	j=IsRegister(user)
	if j[0] == True:
		if int == 1:
			i=arrays.DB_user[j[1]][4]
			if i[1] == "connected":
				return [True,"connected"]
			else:
				return [False,"disconnected"]
		if int == 2:
			return arrays.DB_user[j[1]][1]
		if int == 3:
			return arrays.DB_user[j[1]][0][1]
		if int == 4:
			return arrays.DB_user[j[1]][2]	
		if int == 5:
			return arrays.DB_user[j[1]][3]
		if int == 0:
			return arrays.DB_user[j[1]]
	else:
		return [False, "Not Register"]				

def seguir(i,user,host,opc1="",opc2=""):
	""" Sintaxis: <flags> <usuario> <host> </opcional1> </opcional2>"""
	if info(1,user)[0]:
		if i in info(4,user):
			if info(3,user)==host:
				if opc1.find(opc2) != -1:
					return True
			else:
				client.notice(user,"El host no coincide:01 %s / %s."%(info(3,user),host))	
		else:
			client.notice(user,"Usted no está autorizado para realizar esta operación. 01Requiere: +"+i)		
	else:
		client.notice(user,"Usuario:01 inexistente o Desconectado.")
			
def register(user, host, password):
	a=IsRegister(user)
	if a[0] == False:
		j=[[user, host],password,[],0,["status","connected"]]
		arrays.DB_user.append(j)
		i=IsRegister(user)[0]
		if i == True:
			db.database("API/DB/DB_user",arrays.DB_user).W_db()
			return "Se completo el registro."
		elif i == False:
			return "No se pudo completar el registro."
	else:
		return "Ya se encuentra registrado."

def add_flag(user,flags):
	j=IsRegister(user)
	if j[0] == True:
		for i in flags:
			if i in ["f","j","k","o","p","q","r","s","t","v","F","S"] and not i in arrays.DB_user[j[1]][2]:
				arrays.DB_user[j[1]][2].insert(0,i)
		db.database("API/DB/DB_user",arrays.DB_user).W_db()		
		a=info(4,user)
		a="".join(a)			
		return "Flags(%s): %s" % (user,a)
			
def del_flag(user,flags):
	j=IsRegister(user)
	if j[0] == True:
		for i in flags:
			if i in arrays.DB_user[j[1]][2]:
				a=arrays.DB_user[j[1]][2].index(i)
				del arrays.DB_user[j[1]][2][a]
		db.database("API/DB/DB_user",arrays.DB_user).W_db()		
		a=info(4,user)
		a="".join(a)
		return "Flags(%s): %s" % (user,a)

def logged_out(user,host):
	j=IsRegister(user)
	if j[0] == True:
		if arrays.DB_user[j[1]][4][1] == "connected" and arrays.DB_user[j[1]][0][1] == host:
			del arrays.DB_user[j[1]][4][1]
			del arrays.DB_user[j[1]][0][1]
			arrays.DB_user[j[1]][0].insert(1,"")
			arrays.DB_user[j[1]][4].insert(1,"disconnected")
			if info(1,user)[1]=="disconnected":
				return "disconnected."
			
def logged_in(user, host, password):
	j=IsRegister(user)
	if j[0] == True and info(1,user)[1] != "connected":
		if arrays.DB_user[j[1]][1] == password:
			arrays.DB_user[j[1]][0][1]+=host
			del arrays.DB_user[j[1]][4][1]
			arrays.DB_user[j[1]][4].insert(1,"connected")
			if info(1,user)[1]=="connected":
				return "connected."
		else:
			return "Contraseña/Usuario invalidos."
	else:
		return "Usuario, logueado o inexistente."
		
def find_admin():
	for i in arrays.DB_user:
		if "F" in info(4,i[0][0]):
			return i[0][0]

def admin(target,user):
	for i in arrays.DB_admins:
		i=i.split()
		if target[0] == i[0] and target[1] == i[1]:
			a=add_flag(user, "F")
			return a
