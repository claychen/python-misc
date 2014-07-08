from bs4 import BeautifulSoup

'''
why we can use re.compile to filter a soup?
'''
def main(data):
    import re
    r = re.compile('a.*')
    soup = BeautifulSoup(markup)
    print type(r)
    result = soup.find_all(r)
    for tmp in result:
        print tmp

        
if __name__ == '__main__':
    markup = '''<a>this is a test.</a><ab>the world is beautiful.</ab>
            <c>Although it's full of things we cannot understand.</c>'''
            
    main(markup)
