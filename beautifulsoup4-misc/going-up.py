# -*- coding = utf-8 -*-

#
# TODO clean up 'Going up'(ok) 
#
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup  = BeautifulSoup(html_doc)


#
# Going Down
#
# key functions 
# 	1. a_tag.parent			return the parent 'tag' of a_tag
#	2. a_tag.find_all('tag_str') 	return a 'ResultSet' list of given tag_str

title_tag = soup.title
print title_tag.parent

# title_tag.string.parent is the title_tag itself
print title_tag.string.parent

# print all the parents of tag 'soup.a'
# and soup.panrent.name is '[document]'
for parent in soup.a.parents:
	if parent is None:
		print 'None'
	else:
		print parent.name
