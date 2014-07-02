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
