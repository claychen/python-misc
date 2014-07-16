
import re
p = re.compile('\d+')
ite = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
for match in ite:
    print match 
