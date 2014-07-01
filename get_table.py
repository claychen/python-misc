#!/usr/bin/evn python
# -*- coding:utf-8 -*-


import requests
import logging
import time
try:
	from BeautifulSoup import BeautifulSoup
except ImportError:
	from bs4 import BeautifulSoup as BeautifulSoup_
	try:
		import html5lib
		BeautifulSoup = lambda page: BeautifulSoup_(page, 'html5lib')
	except ImportError:
		BeautifulSoup = lambda page: BeautifulSoup_(page, 'html.parser')
'''
This tiny piece code segment is inspired by another project for downloading
lecture resources from Coursera classes. The project's home is at:
https://github.com/jplehmann/coursera
Thanks for this wonderful work! If this segment didn't use original lecense 
properly, please let me know. Thanks!
'''
def get_page(session, url):
	r = session.get(url)
	
	try:
		r.raise_for_status()
	except request.exceptions.HTTPError as e:
		logging.error("Error %s getting pages %s", e, url)
		raise
	return r.text

def main(): 
	try:
		href = 'https://tw.stock.yahoo.com/q/q?s=2412'
		session = requests.Session()
		s_time = time.time()
		page = get_page(session, href)
		e_time = time.time()
		print ( str(e_time - s_time) + ' was costed to get a page.' )
	except requests.exceptions.HTTPError:
		return None

	soup = BeautifulSoup(page)
	#print(soup.prettify()) 
	# using BequtifulSoup 3 
	if soup is None:
		print('soup is none')

	# align="center" bgcolor="#FFFfff" nowrap
	head = []
	for th in soup.find_all(['th'], width='55'):
		head.append(th.text)
	value = []
	for td in soup.find_all(['td'], bgcolor='#FFFfff'):
		value.append(td.text)
	for i in range(0,len(head)):
		print ( head[i] + ' ' + value[i].rstrip() )
	# /logos/doodles/2014/world-cup-2014-42-4675815216250880-hp.gif 
	'''
	l = soup.find(attrs={'type':'img'})
	if l is not None:
		print( l['src'] )
	'''
if __name__ == '__main__':
	main()


'''
Add an example to deal with html table
1. http://nbviewer.ipython.org/github/muxuezi/bs4test/blob/master/bs4test.ipynb
https://github.com/muxuezi/bs4test

TODO : I need to familiar with BeautifulSoup4 API
'''
