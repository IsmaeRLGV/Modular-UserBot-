#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arrays
def parce_nick_modes(mode_string):
	return _parce_modes(mode_string, "")
def parce_channel_modes(mode_string):
	return _parce_modes(mode_string, "bklvohq")
def _parce_modes(mode_string, unary_modes=""):
	if not mode_string or not mode_string[0] in '+-':
		return []
	modes = []
	parts = mode_string.split()
	mode_part, args = parts[0], parts[1:]
	for ch in mode_part:
		if ch in "+-":
			sign = ch
			continue
		arg = args.pop(0) if ch in unary_modes and args else None
		modes.append([sign, ch, arg])
	return modes				

def name_mode(user,parce_mode):
	modes={"o":"op","v":"voice","h":"halfop",
	       "q":"quit","b":"ban","e":"excepcion"}
	amode={"m":"+m","l":"limite","k":"contraseña",
	       "i":"solo invitados","j":"j","s":"+s","r":"+r"}  
	for i in parce_mode:
		try:
			if i[0] == '+':
				print user+" da "+modes[i[1]]+" ha "+ i[2]
			if i[0] == '-':
				print user+" quita "+modes[i[1]]+" ha "+ i[2]
		except KeyError:
			try:
				if i[0] == '+':
					print user+" establece "+amode[i[1]]
				if i[0] == '-':
					print user+" quita el "+amode[i[1]]
			except KeyError:
				pass	
				
