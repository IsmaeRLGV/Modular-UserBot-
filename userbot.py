#!/usr/bin/env python
# -*- coding: utf-8 -*-
from API import arrays,db,modes,connection,client,google,evaluate,privs,WAI,sgb
import datetime,string,socket,time,re
s=connection.s
readbuffer=connection.readbuffer
while True:
	now = datetime.datetime.now()
	time2= datetime.time(now.hour, now.minute, now.second)
	readbuffer=readbuffer+s.recv(1024)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop( )
	for j in temp:
		print j
		j=string.rstrip(j)
		try: # Sistema de entrada de informacion.
			mlen = j.split()
			#print "|||--+%s "%mlen
			host=mlen[0].split('@')[1]
			#print "|||-+-%s"%host
			chan=mlen[2]
			#print "|||+++%s"%chan			
			user=j.split('!')[0].split(':')[1]
			#print "|||+--%s"%user
			mlex=j.split("%s %s %s :"%(mlen[0],mlen[1],mlen[2]))[1]
			#print "|||-++%s"%mlex
			mlenx=mlex.split()
			#print "[%s] <%s> %s\r"%(time2, user, mlex)
		except IndexError:
			if mlen[0]=="PING":
				mlex="None"
				mlenx="None"
				host="None"
				user="None"
				chan="None"
				client.send_msg("PONG " + mlen[1])
					
		try: # Sistema de Identificación, Control de Usuarios/Admins/Flags. 
			if mlenx[0].find("%sregistro" % arrays.comd) != -1:
				client.privmsg(user,privs.register(user, host, mlenx[1]))
				client.privmsg(user,"Usuario: 12%s; Host: 12%s; Password: 12%s."%(user, host, mlenx[1]))
			if mlenx[0].find("%slogout" % arrays.comd) != -1:
				client.privmsg(user,"05%s"%privs.logged_out(user, host))
			if mlenx[0].find("%slogin"%arrays.comd) != -1:
				client.privmsg(user,"09%s" % privs.logged_in(user, host,mlenx[1]))
			if mlenx[0].find("%sadmin"%arrays.comd) != -1:
				client.privmsg(user, privs.admin([mlenx[1],mlenx[2]],user))
			if mlenx[0].find("%sinfo" % arrays.comd) != -1:
				if privs.seguir("F",user,host):
					try: i=int(mlenx[1])
					except ValueError: i=0
					client.privmsg(user, privs.info(i,mlenx[2]))	
			if mlenx[0].find("%sflags" % arrays.comd) != -1:
				if privs.seguir("f",user,host) or privs.seguir("F",user,host):
					p_mode=modes.parce_nick_modes(mlenx[1])
					for i in p_mode:
						if i[0]=="+" and i[1]!="F" and user!=mlen[2]:
							privs.add_flag(mlenx[2],i[1])
						elif "F" in privs.info(4,user) and i[0]=="+":
							privs.add_flag(mlenx[2],i[1])
						if i[0] == "-":
							privs.del_flag(mlenx[2],i[1])
					client.privmsg(chan,"Flags(%s): %s"%(mlenx[2],"".join(privs.info(4,mlenx[2]))))
		except (NameError, IndexError):
			pass
		
		try: # Sistema de eventos
			a=sgb.conv_type(mlen[1]).conv_int()
			if type(a) == type(int(0)):
				if a==376:
					client.Join(arrays.CHAN)
					client.send_msg("PRIVMSG NickServ :IDENTIFY f4mil1a")
				if a==401:
					mlenx=[] # Debug
				if a==403: 
					mlen=[]  # Debug		
				if a==404:
					mlen=[]  # Debug
				if a==473:
					client.privmsg("ChanServ","INVITE "+mlen[3])
				if a==474:
					client.privmsg("ChanServ","UNBAN "+mlen[3])
					client.Join(mlen[3])
				if a==475:
					client.privmsg("ChanServ","GETKEY "+mlen[3])
			if mlen[1] in ["PART", "JOIN", "NICK", "QUIT"]:
				j=evaluate.InChannel(user)
				if mlen[1]=="JOIN":
					if user==arrays.NICK:
						arrays.ls_chans.append(chan)
					if j is None:
						arrays.ls_users.append([user,[chan]])
					else:
						arrays.ls_users[j[1]][1].insert(0,chan)
				if  j is None:
					pass
				elif j[0] == True:
					if mlen[1]=="PART":
						arrays.ls_users[j[1]][1].remove(chan)
					if mlen[1]=="NICK":
						del arrays.ls_users[j[1]][0]
						arrays.ls_users[j[1]].insert(0,mlenx[0])
					if mlen[1]=="QUIT":
						del arrays.ls_users[j[1]]
			if mlen[1] in ["KICK","MODE","INVITE"]:
				if mlen[1]=="KICK":
					if mlen[3]==arrays.NICK and user!=arrays.NICK:
						client.Join(chan)
					elif mlen[3]!=arrays.NICK and user!=arrays.NICK and arrays.MOD_ukik[0]=="on":
						client.kick(chan,user,"AntiKick")
				if mlen[1]=="MODE":
					p_mode=modes.parce_channel_modes(j.split(" MODE %s "%chan)[1])
					for i in p_mode:
						if i[0] == "+":
							if i[1]=="o"and arrays.MOD_aop[0]=="on" and user!=arrays.NICK:
								client.mode(chan,"-o",i[2])
						else:
							if i[1]=="o" and i[2]==arrays.NICK:
								client.privmsg("ChanServ","OP "+chan)				
				if mlen[1]=="INVITE":
					client.Join(mlenx[0])
				mlenx=[] # Debug
			if arrays.MOD_BadW[0]=="on" and user!=arrays.NICK and mlenx!=[]:
				E0=re.compile(r'pu(t|th)(a|o)|(g|h|w)uev(o|a)|mari(c|k)(o|a)|joder|idio(t|th)(a|e)|ca(b|v)ron|novi(o|a)|mierd(a|e)|coñ(o|a)|pene|ma(l|r)dit(a|o)|pendej(a|o)|estupid(a|o)|cul(o|ea)|(b|v)astard(a|o)|chupalo|mamal(a|o)|sexo|co(g|j)(i|e|o)|porno|fo(y|ll)a|perra|mmg|hp|an(al|o)', re.IGNORECASE)
				Seguir = True
				while Seguir==True:
					for i in mlenx:
						if E0.match(i):
							client.kick(chan,user,"12RAZÓN DE EXPULSIÓN: 04Mala Palabra. Si esto es un error notifique a: 03%s."%privs.find_admin())
							Seguir=False
					Seguir=False					
			if mlenx[0].find("VERSION") != -1:
				client.ctcp_version(user)
			if mlenx[0].find("PING") != -1:
				client.ctcp_ping(user,mlenx[1])	
		except (IndexError,NameError):
			pass		
		try: # Funciones con requerimientos especiales (Flags,etc...).
			if mlenx[0].find("%smod"%arrays.comd) != -1:
				if privs.seguir("F",user,host):
					n=re.compile(r'%s'%mlenx[1], re.IGNORECASE)
					if n.match("AntiOp"):
						client.privmsg(chan,evaluate.antiop(mlenx[2])[1])
					if n.match("BadWords"):
						client.privmsg(chan,evaluate.badwords(mlenx[2])[1])
					if n.match("AntiKick"):
						client.privmsg(chan,evaluate.antikick(mlenx[2])[1])
			if mlenx[0].find("%sop"%arrays.comd)!=-1 or mlenx[0].find("%sdeop"%arrays.comd)!=-1:
				if privs.seguir("o",user,host):
					if mlenx[0]=="%sop"%arrays.comd: e='+'
					else: e='-'
					try: client.mode(chan,e+"o",mlenx[1])
					except IndexError: client.mode(chan,e+"o",user)
			if mlenx[0].find("%sv"%arrays.comd)!=-1 or mlenx[0].find("%sdv"%arrays.comd) != -1:
				if privs.seguir("v",user,host):
					if mlenx[0]==arrays.comd+"v": e='+'
					else: e='-'
					try: client.mode(chan,e+"v",mlenx[1])
					except IndexError: client.mode(chan,e+"v",user)
			if mlenx[0].find("%sk"%arrays.comd) != -1:
				if privs.seguir("k",user,host):
					try: client.kick(chan,mlenx[1],mlex.split("%s %s "%(arrays.comd+"k",mlenx[1]))[1])
					except IndexError: client.kick(chan,mlenx[1])														
			if mlenx[0].find("%sFL"%arrays.comd) != -1:
				if privs.seguir("f",user,host):
					client.privmsg("ChanServ","FLAGS %s %s %s"%(chan,mlenx[1],mlenx[2]))
			if mlenx[0].find("st"+arrays.comd) != -1:
				if privs.seguir("f",user,host):
					client.privmsg("ChanServ","SET %s %s %s"%(chan,mlenx[1],mlenx[2]))						
			if mlenx[0].find("%sctrl"%arrays.comd) != -1:
				if privs.seguir("s",user,host):
					if mlenx[1]=="join":
						try: client.Join(mlenx[2],mlenx[3])
						except IndexError: client.Join(mlenx[2])
					if mlenx[1]=="part":
						client.part(mlenx[2],"SALIDA ORDENADA.")
			if mlenx[0].find("%simagen"%arrays.comd) != -1:
				element=mlex.split(arrays.comd+"imagen ")[1]
				google.google(chan,element).images()					
			if mlenx[0].find("%sgoogle"%arrays.comd) != -1:
				element=mlex.split("%sgoogle "%arrays.comd)[1]
				google.google(chan,element).search()
			if mlenx[0].find("%sip"%arrays.comd)!=-1:
				WAI.ip_info(chan,mlenx[1])															
		except (IndexError,NameError):
			pass	
