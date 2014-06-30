#!/usr/bin/evn python
# -*- coding:utf-8 -*-


import requests
import logging
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
	page = '' 
	try:
		href = 'http://www.google.com.tw/'
		session = requests.Session()
		page = get_page(session, href)
		#print(page)
	except reuqests.exceptions.HTTPError:
		return None

	soup = BeautifulSoup(page)
	#print(soup.prettify()) 
	# using BequtifulSoup 3 
	if soup is None:
		print('soup is none')
	for img in soup.find_all(['img']):
		print img['src'] 
	# /logos/doodles/2014/world-cup-2014-42-4675815216250880-hp.gif 
	'''
	l = soup.find(attrs={'type':'img'})
	if l is not None:
		print( l['src'] )
	'''
if __name__ == '__main__':
	main()
