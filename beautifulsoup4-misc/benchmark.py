'''
Referenced source code of BeautifulSoup in bs4/diagnose.py
'''
import sys
import traceback
import time
from bs4 import BeautifulSoup
def print_parse( parser , time):
	print '%s parsed the markup in %.5f ' % (parser, time)

def benchmark(data):
	for parser in ['lxml',['lxml','html'],'html5lib', 'html.parser']:
		try:
			a = time.time()
			soup = BeautifulSoup( data, parser )
			b = time.time()
			print_parse( 'bs4+' + str(parser) , b-a )
		except Exception, e:
			print 'error msg: ' + e.message
			traceback.print_exc()
	try:
		from lxml import etree
		a = time.time()
		etree.HTML(data)
		b = time.time()
		print_parse( 'Raw lxml', b-a)
		
		import html5lib
		parser = html5lib.HTMLParser()
		a = time.time()
		parser.parse(data)
		b = time.time()		
		print_parse( 'Raw html5lib', b-a)
	except Exception, e:
		print 'error msg: ' + e.message
		traceback.print_exc()
	
if __name__ == '__main__':
	benchmark(sys.stdin.read())
