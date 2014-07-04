from bs4 import BeautifulSoup

markup = '''
<div>This document contains a <!DOCTYPE surprise>surprise doctype</div>
'''
print 'Markup:' + markup

soup = BeautifulSoup(markup, 'lxml')
print 'lxml:'
print soup.div.encode('utf-8')

soup = BeautifulSoup(markup, 'html5lib')
print 'html5lib:' 
print soup.div.encode('utf-8')

soup = BeautifulSoup(markup, 'html')
print 'html:'
print soup.div.encode('utf-8')
