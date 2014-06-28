'''
Programe name : filerename.py
Arthur : Clay Chen
Usage : Rename files by the prefix string and index.
Example : python filerename.py ./notes Week4_
'''

import sys,os,time,re
path = sys.argv[1]
prefix = sys.argv[2]

os.chdir(path)
timelist = []
for f in os.listdir('.'):
	print("%s %s " % (os.path.getmtime(f),time.ctime(os.path.getmtime(f))))
	if re.search('png$', f):
		timelist.append(os.path.getmtime(f))
	#(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(i)
	#print("last modified %s " % time.ctime(mtime) )

timelist.sort()

for f in os.listdir('.'):
	#print( "# %d : %s " % (timelist.index(os.path.getmtime(f) ),f ))
	if re.search('png$', f):
		os.rename(f, prefix+str(timelist.index(os.path.getmtime(f)))+'.png')
