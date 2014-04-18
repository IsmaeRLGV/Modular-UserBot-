#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson,socket,urllib2,client
from urllib import *
	
class google:
	def __init__(self,target,query):
		self.query=query
		self.target=target
	def search(self):
		ut=[]
		q=urlencode({'q' : self.query})
		rs_search=urlopen("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s" % q)
		json = simplejson.loads(rs_search.read())
		results = json['responseData']['results']
		for i in results:
			ut.append("%s 11%s" % (i['titleNoFormatting'],i['url']))
		client.privmsg(self.target,"Resultados de la busqueda de 12G04o08o12g03l04e:")
		client.privmsg(self.target,"13|".join(ut))
	def images(self):
		u=[]			
		search=quote_plus(self.query)
		ip=socket.gethostbyname(socket.gethostname())
		size="imgsz=small|medium|large|xlarge"
		results = "rsz=1"
		url=('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q=%s&userip=%s&as_filetype=png|jpg&%s&%s' % (search, ip, size, results))
		request=urllib2.Request(url, None, {'Referer': 'http://bobbelderbos.com' })
		response = urllib2.urlopen(request)
		json = simplejson.load(response)
		results = json['responseData']['results']
		for i in results:
			u.append("11%s" % i['url'])
		gh="12G04o08o12g03l04e 12I04m08a12g03e04n: "	
		client.privmsg(self.target,gh+"11".join(u))
class google_translate(object):
	LANG_ARABIC = "ar"
	LANG_CHINESE = "zh"
	LANG_ENGLISH = "en"
	LANG_FRENCH = "fr"
	LANG_GERMAN = "de"
	LANG_ITALIAN = "it"
	LANG_JAPANESE = "ja"
	LANG_KOREAN = "ko"
	LANG_PORTUGESE = "pt"
	LANG_RUSSIAN = "ru"
	LANG_SPANISH = "es"
	def __init__(self, proxy):
		self.languages = {LANG_ARABIC:_("Arabic"), LANG_CHINESE:_("Chinese"), LANG_ENGLISH:_("English"),
		                  LANG_FRENCH:_("French"), LANG_GERMAN:_("German"), LANG_ITALIAN:_("Italian"),
		                  LANG_JAPANESE:_("Japanese"), LANG_KOREAN:_("Korean"), LANG_PORTUGESE:_("Portugese"),
		                  LANG_RUSSIAN:_("Russian"), LANG_SPANISH:_("Spanish")}		             
		self.proxy = proxy
	def translate(self, src, dst, text):
		socket.setdefaulttimeout(10)
		opener = self.proxy.get_http_opener()
		pair = src + "|" + dst
		params = urlencode({'langpair': pair, 'text': text.encode("utf8")})
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		f = opener.open("http://translate.google.com/translate_t?%s" % params)
		response = str(f.read())
		result_box = response.find("<div id=result_box dir=")
		if result_box == -1:
			return "Error: Google-Translate."
		target = response[result_box:]
		end = target.find("</div>")
		translate = "<body><p>" + target[29:end] + "</p></body>"
		return translate	
