#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arrays
status={1:"on",2:"off"}

def InChannel(user):
	for i in arrays.ls_users:
		if user==i[0]:
			posc=arrays.ls_users.index(i)
			return (True,posc)		

def antiop(target):
	target=target.split()
	try:
		if target[0] == status[1] and not status[1] in arrays.MOD_aop:
			del arrays.MOD_aop[0]
			arrays.MOD_aop.append(status[1])
			return (True,"AntiOp " + status[1])
		elif target[0] == status[1] and status[1] in arrays.MOD_aop:
			return (None,"Ya se encuentra en: " + status[1])
		if target[0] == status[2] and not status[2] in arrays.MOD_aop:
			del arrays.MOD_aop[0]
			arrays.MOD_aop.append(status[2])
			return (False,"AntiOp " + status[2])
		elif target[0] == status[2] and status[2] in arrays.MOD_aop:
			return (None,"Ya se encuentra en: " + status[2])
	except IndexError:
		return [None,"Fuera de rango."]
def badwords(target):
	target=target.split()
	try:
		if target[0] == status[1] and not status[1] in arrays.MOD_BadW:
			del arrays.MOD_BadW[0]
			arrays.MOD_BadW.append(status[1])
			return (True,"AntiBadwords " + status[1])
		elif target[0] == status[1] and status[1] in arrays.MOD_BadW:
			return (None,"Ya se encuentra en: " + status[1])
		if target[0] == status[2] and not status[2] in arrays.MOD_BadW:
			del arrays.MOD_BadW[0]
			arrays.MOD_BadW.append(status[2])
			return (False,"AntiBadwords " + status[2])
		elif target[0] == status[2] and status[2] in arrays.MOD_BadW:
			return (None,"Ya se encuentra en: " + status[2])	
	except IndexError:
		return (None,"Fuera de rango.")
def antikick(target):
	target=target.split()
	try:
		if target[0] == status[1] and not status[1] in arrays.MOD_ukik:
			del arrays.MOD_ukik[0]
			arrays.MOD_ukik.append(status[1])
			return (True,"AntiKick " + status[1])
		elif target[0] == status[1] and status[1] in arrays.MOD_ukik:
			return (None,"Ya se encuentra en: " + status[1])
		if target[0] == status[2] and not status[2] in arrays.MOD_ukik:
			del arrays.MOD_ukik[0]
			arrays.MOD_ukik.append(status[2])
			return (False,"AntiKick " + status[2])
		elif target[0] == status[2] and status[2] in arrays.MOD_ukik:
			return (None,"Ya se encuentra en: " + status[2])	
	except IndexError:
		return (None,"Fuera de rango.")       
