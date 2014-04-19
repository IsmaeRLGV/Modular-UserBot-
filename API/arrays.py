#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import *
PORT=db("API/DB/PORT").open_db()
CHAN=db("API/DB/CHAN").open_db()
HOST=db("API/DB/HOST").open_db()
NICK=db("API/DB/NICK").open_db()
IDENT=NICK
REALNAME=NICK
comd=db("API/DB/DB_comd").open_db()
DB_user=db("API/DB/DB_user").open_db()
DB_admins=db("API/DB/DB_admins").open_db()
# Temporales
ls_users=[]
ls_chans=[]

# Mods
MOD_BadW = ["off"]
MOD_ukik = ["off"]
MOD_aop  = ["off"]

