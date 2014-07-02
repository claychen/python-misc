# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

doc = ['<p id="firstpara" align="center">This is paragraph <b>one</b> '
       'of ptyhonclub.org.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b> '
       'of pythonclub.org.']

soup = BeautifulSoup(''.join(doc))

#
# TAG Object: get the first 'p' tag 
#
print '===TAG Object==='
tag = soup.p

# the type of tag is bs4.element.Tag 
print type(tag)
# get 'p' tag name, in this case, it just p
tag.name

# get 'p' tag attribute
print 'id: ' + tag['id']

# list 'p' tag attributes
print 'attrs: ' 
print tag.attrs

# print content of 'p'
print tag.text

# modify tag's name into 'paragraph' 
tag.name = 'paragraph'
print tag

# del tag's id
del tag['id']
print tag

#
# multi-valued attributes
#
print '===multi-valued attributes==='
css_soup = BeautifulSoup("<p class='body strikeout'></p>")
print css_soup.p['class']

id_soup = BeautifulSoup('<p id="my id"></p>')
print id_soup.p['id']

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
rel_soup.a['rel'] # ['index']
rel_soup.a['rel'] = ['index', 'contents']
print rel_soup.p # <p>Back to the <a rel="index contents">homepage</a></p>

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print xml_soup.p['class'] # u'body strikeout'

#
# NavigableString
#
soup = BeautifulSoup('<p>To err is human</p>')
print type(soup.p.string)
print unicode(soup.p.string)
soup.p.string.replace_with('not devine')
print soup.p


