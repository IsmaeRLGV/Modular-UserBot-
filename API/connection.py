#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket,arrays,time
conectado = False
veces= 0
s=socket.socket()
readbuffer=""
print "Buscando " + arrays.HOST
while conectado==False:
	try:
		s.connect((arrays.HOST, arrays.PORT))
		print 'Conectado. Ahora registrandose'
		conectado = True
	except socket.gaierror:
		veces += 1
		print 'Error N-%s\nReintentando...' % veces
		if veces == 30:
			print 'Se ha superado el numero maximo de intentos.'
			exit()
		conectado = False
if conectado:
	s.send("NICK %s\n" % arrays.NICK)
	s.send("USER %s %s * * :%s\r\n" % (arrays.IDENT, arrays.NICK , arrays.REALNAME))
