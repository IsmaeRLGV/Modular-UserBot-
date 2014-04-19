#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import client
def ayuda(user,target="None"):
	__ayuda=re.compile(r'%s' % target, re.IGNORECASE)
	if __ayuda.match('flags'):
		client.notice(user, "Ayuda para: Flags")
		client.notice(user, "+v - Habilita el uso para los comandos v/dv.")
		client.notice(user, "+o - Habilita el uso para los comandos op/deop.")
		client.notice(user, "+k - Habilita el uso para el comando k.")
		client.notice(user, "+s - Habilita el uso para el comandos ctrl.")
		client.notice(user, "+f - Habilita el uso para los comandos FL/st.")
		client.notice(user, "+F - Otorga acceso completo de administrador.")
	else:
		comm_des={'v':"Otorga voice al usuario especificado ó al dador de la orden. Syntax: v <nickname>.",
		          'dv':"Quita voice al usuario especificado ó al dador de la orden. Syntax: dv <nickname>.",
		          'op':"Otorga op al usuario especificado ó al dador de la orden. Syntax: op <nickname>.",
		          'deop':"Quita op al usuario especificado ó al dador de la orden. Syntax: deop <nickname>.",
		          'k':"Expulsa al usuario especificado. Syntax: k <nickname> <optional comment>.",
		          'ctrl':"Controla segmentos especificos del BOT. Syntax: ctrl <target> <channel>; Targets list: join, part.",
		          'FL':"Otorga flags al usuario especificado via ChanServ. Syntax: FL <target> <user>",
		          'st':"Cambia los seteos de ChanServ. st <command> <target>",
		          'register':"Registra al usuario en el BOT. Syntax: register <password>",
		          'logout':"Se desconecta la cuenta del BOT. Syntax: logout",
		          'login':"Se conecta la cuenta del BOT. Syntax: login <password>",
		          'admin':"Se identifica como adminstrador del BOT. Syntax: admin <user> <password>",
		          'info':"Muestra la informacion del usuario especificado. Syntax: <user>",
		          'mod':"Cambia los modos del BOT. Syntax: mod <ModName> <target>; Mods Names: Antiop BadWords AntiKick",
		          'imagen':"Busca una imagen de lo especificado. Syntax: imagen <Contenido para la Busqueda>",
		          'google':"Realiza una busqueda en google de los especificado. Syntax: google <Contenido para la Busqueda>",
		          'ip':"Muestra la informacion de la IP especificada. Syntax: ip <ip>"
		          }
		client.notice(user, comm_des.get(target, "El comando no existe o no hay una descripcion para el"))
