#!/usr/bin/env python
# -*- coding: utf-8 -*-
from API.db import *
import os,time,random,re
clear=lambda: os.system("clear")
cont="s"
print "Bienvenido a la configuración de UserBot."
print "Nota: Algunos segmentos requridos u opcionales dejarlos en blanco si no sabes para que sirve.\n\n"
while cont != "*":
	print "Marque:","\n 1-Para editar el nick,puerto,canal,etc.","\n 2-Gestionar administradores (bot).","\n 3-Para salir."
	try:
		cont=int(raw_input("->> "))
	except ValueError:
		print "El valor ingresado no es un numero.\n"
		exit()
	if cont == 1:
		clear()
		print "LEYENDA: Opcional: * Requerido: +"
		print "Ingrese algunos datos necesarios."		
		HOST=raw_input("Servidor           + >>> ")
		if HOST == "":
			HOST = "irc.freenode.net"
		try:
			PORT=int(raw_input("Puerto             * >>> "))
		except ValueError:
			PORT=6667	
		CHAN=raw_input("Canal Principal    + >>> ")
		if CHAN == "":
			CHAN = "#gazuza"
		NICK=raw_input("Nickname           + >>> ")
		if NICK == "":
			NICK = "UserBot"	
		comd=raw_input("Inicio de Comandos * >>> ")
		if comd == "":
			comd = "!"
		database("API/DB/HOST",HOST).W_db()
		database("API/DB/PORT",PORT).W_db()
		database("API/DB/CHAN",CHAN).W_db()
		database("API/DB/NICK",NICK).W_db()
		database("API/DB/DB_comd",comd).W_db()
		database("API/DB/DB_user",[[["UserBot", "127.0.0.7"],"password",[],0,["status","connected"]]]).W_db()
		clear()
		print "Servidor: " + HOST
		print "Puerto: %s" % PORT
		print "Canal Principal: " + CHAN
		print "Nick: " + NICK
		print "Inicio de Comandos: " + comd
	if cont == 2:
		print "¿Que desea hacer?","\n1 - Agregar Administradores","\n2 - Eliminar Administradores"
		try:
			EE0=int(raw_input("->> "))
		except ValueError:
			EE0=9
		if EE0 == 1:
			clear()
			print "LEYENDA: Opcional: * Requerido: +"
			user=raw_input("Usuario >>> ")
			cont2=raw_input("¿Desea autogenerar la clave?\nS/n >>> ")
			ready_passw=False
			if cont2 == "S" or cont2 == "s":
				ii=('o','j','k','9','h','l','a','u','7','3','b','0','p','m','c','w','f','d','x','4','r','1','e','2','g','5','q','6','8','t','y','i','s','z','v','n','O','J','K','H','L','A','U','B','P','M','C','W','F','D','X','R','E','G','Q','T','Y','I','S','Z','V','N')
				hash_=''
				for iii in range(30):
					code=random.choice(ii)
					while code in hash_:
						code=random.choice(ii)
					hash_=code+hash_
					password=hash_
					ready_passw=True
			if cont2== "N" or cont2 == "n":
				ready=""
				while not "n" in ready:
					ready=""
					characters=0
					password=raw_input("password >>> ")
					numeric=re.search("\d", password)
					string_mayus=re.search("[A-Z]",password)
					string_minus=re.search("[a-z]",password)
					if numeric:
						ready+="s"
					if string_mayus:
						ready+="s"
					if string_minus:
						ready+="s"
					for i in password:
						characters+=1
						if characters == 30:
							ready+="s"
					if ready=="ssss":
						ready_passw=True
						ready+="n"
					else:
						print "La clave ingresada no cumple con las condiciones."
			if ready_passw:
				clear()
				print "Usuario: " + user
				print "Password: " + password
				try:
					import API.arrays
					API.arrays.DB_admins.append("%s %s" % (user,password))
					print "Se añadio a la Base de Datos."
				except AttributeError:
					ee="%s %s" % (user,password)
					database("API/DB/DB_admins", [ee]).a_db()
					print "Se creo y añadio a la Base de Datos."
					exit()
	if cont == 3:
		print "Saliendo..."
		exit() 				
