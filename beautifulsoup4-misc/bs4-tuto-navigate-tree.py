# -*- coding = utf-8 -*-

#
# TODO clean up 'Going Down'(ok) 
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
# 	1. a_tag.'tag_str'		return the value of first tag_str in subtree
#	2. a_tag.find_all('tag_str') 	return a 'ResultSet' list of given tag_str
#	3. a_tag.contents 		return a 'list' which is a subtree of a_tag
#	4. a_tag.children		return a 'listgenerator'
#	5. a_tag.descendants		return a 'listgenerator'
print soup.head
print soup.title
print soup.body.b
print soup.a

print "get all '<a>' in soup: "
print soup.find_all('a')

head_tag = soup.head
print 'head_tag: '
print head_tag
print 'head_tag.contents: '
print head_tag.contents

# get the first children of subtree 
title_tag = head_tag.contents[0]
print 'title tag = head_tag.contents[0] :'
print title_tag

# get the number of children of soup
print 'the #(children) and #(descendant) of soup: '
print len(soup.contents) 
print len(list(soup.children))
print len(list(soup.descendants))
print 'the tag name of first children of soup: '
print soup.contents[0].name # html tag

# get all childrens of a tag
for child in title_tag.children:
	print(child)

# get descendants
for child in head_tag.descendants:
	print(child)


