#!/usr/bin/env python
# -*- coding: utf-8 -*-
import connection
import socket,time
s=connection.s
def send_msg(msg):
	"""Send Msg. """
	s.send("%s\r\n"%msg)
	
def pasm(msg):
	"""Print And Send Msg."""
	time.sleep(1)
	s.send("%s\r\n"%msg)
	print "<<< " + msg

def privmsg(target,text):
	"""Send a PRIVMSG command."""
	pasm("PRIVMSG %s :%s" % (target, text))

def notice(target,text):
	"""Send a NOTICE command."""
	pasm("NOTICE %s :%s" % (target, text))

def Join(channel, key=""):
	"""Send a JOIN command."""
	if channel!="0":
		pasm("JOIN %s%s" % (channel, (key and (" " + key))))

def part(channel, message=""):
	"""Send a PART command."""
	pasm("PART %s%s" % (channel, (message and (" :" + message))))
	
def kick(channel, nick, comment=""):
	"""Send a KICK command."""
	pasm("KICK %s %s%s" % (channel, nick, (comment and (" :" + comment))))

def remove(channel, nick, comment=""):
	"""Send a REMOVE command."""
	pasm("REMOVE %s %s%s" % (channel, nick, (comment and (" :" + comment))))

def mode(channel, target, command=""):
	"""Send a MODE command."""
	pasm("MODE %s %s%s" % (channel, target, (command and (" " + command))))

def topic(channel, new_topic=None):
	"""Send a TOPIC command."""
	if new_topic is None:
		pasm("TOPIC " + channel)
	else:
		pasm("TOPIC %s :%s" % (channel, new_topic))
def ctcp_version(user):
	send_msg("NOTICE %s :IRCBot. UserBot by Kwargs." % user)
def ctcp_ping(user,target):
	s.send("NOTICE %s :PING  %s\n"%(user,target))
