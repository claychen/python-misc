# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup

#
# a_tag.next_sibling		return next sibling 'tag' of a_tag
# a_tag.prevous_sibling 	return previous sibling 'tag' of a_tag
# the previous two function coud return u',\n' if '\n' is in a_tag's sibling
# a_tag.next_siblings		return generator of next siblings
# a_tab.prevous_siblings 	return generator of previous siblings

sibling_soup = BeautifulSoup('<a><b>text1</b><c>text2</c></b></a>')

# c
sibling_soup.b.next_sibling 

# b
sibling_soup.c.previous_sibling

soup = BeautifulSoup('''
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
''')

# u',\n'
soup.a.next_sibling

for sibling in soup.a.next_siblings:
	print ( repr(sibling) )

for sibling in soup.find(id='link3').previous_siblings:
	print ( repr(sibling) )

