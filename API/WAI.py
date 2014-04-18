#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib,urllib2
from re import *
import client
"""This modules is With Access Internet (W.A.I)"""

def ip_info(target,ip):
	u=[["12Informacion General:"],["12Geolocalización:"]]
	E=[]
	url="http://whatismyipaddress.com/ip/"+ip
	raw=urllib.urlopen(url).read()
	E0=search('<tr><th>IP:</th><td>([\w\W]+)</td></tr>',raw)
	E1=search('<tr><th>ISP:</th><td>([\w\W]+)</td></tr>', raw)
	E2=search('<tr><th>Organization:</th><td>([\w\W]+)</td></tr>', raw)
	E3=search('<tr><th>Services:</th><td>([\w\W]+)</td></tr>',raw)
	
	E4=search('<tr><th>Country:</th><td>([\w\W]+) <img src=', raw)
	E5=search('<tr><th>State/Region:</th><td>([\w\W]+)</td></tr>', raw)
	E6=search('<tr><th>City:</th><td>([\w\W]+)</td></tr>', raw)
	
	if E0:u[0].append("15 IP:01 %s"%E0.groups()[0].split("</td></tr>")[0])
	else: u[0].append("15 IP:04 N/A")
	if E1: u[0].append("15 ISP:01 %s"%E1.groups()[0].split("</td></tr>")[0])
	else: u[0].append("15 ISP:04 N/A")
	if E2: u[0].append("15 Organización:01 %s"%E2.groups()[0].split("</td></tr>")[0])
	else: u[0].append("15 Organización:01 N/A")
	if E3: u[0].append("15 Servicios:04 %s"%E3.groups()[0].split("</td></tr>")[0])
	else: u[0].append("15 Servicios:04 N/A")
	
	if E4: u[1].append("15 Pais:01 %s"%E4.groups()[0].split("</td></tr>")[0])
	else: u[1].append("15 Pais:04 N/A")
	if E5: u[1].append("15 Estado:01 %s"%E5.groups()[0].split("</td></tr>")[0])
	else: u[1].append("15 Estado:04 N/A")
	if E6: u[1].append("15 Ciudad:01 %s"%E6.groups()[0].split("</td></tr>")[0])
	else: u[1].append("15 Ciudad:04 N/A")
	
	for i in u:
		E.append(",".join(i))
	client.privmsg(target," ".join(E))
	
def tittle_page(query):
	if search('(.+://)(www.)?([^/]+)(.*)', query):
		raw = urllib2.urlopen(query).read()
		t=search('<title>([\w\W]+)</title>', raw).groups()[0]
		T=''
		for o in titulo.split('\n'):
			T=o.lstrip()+' '
		return T
