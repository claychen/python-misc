
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#
# a_tag.next_element		return the next 'tag' element to be parsed 
# a_tag.previous_element	return the previous 'tag' element to be parsed
# a_tag.next_elements		return iterator to move backward or forward in
# a_tag.previous_elements		the document as it was parsed. 

soup = BeautifulSoup(html)

link = soup.find('a', id='link3')
# ';and the lived at the bottom of a well.
print link.next_sibling
# u'Tillie'
print link.next_element

print link.previous_element

# use iterator to move forward or backward in the document as it was parsed.
for element in link.next_elements:
	print repr(element)

