#
# use @property @xxx.setter @xxx.deleter to specify getter, 
# setter and deleter for the variable of a object
class Dog(object):
	def __init__(self):
		self._fname = None
		self._sname = None

	@property
	def fname(self):
		print  "Getting Dog's first name"
		return self._fname
	@fname.setter
	def fname(self, value):
		print "Setting Dog's first name"
		self._fname = value
	@fname.deleter
	def fname(self):
		del self._fname

	@property
	def sname(self):
		print "Getting Dogs's second name"
		return self._sname
	@sname.setter
	def sname(self, value):
		print "Setting Dog's second name"
		self._sname = value
	@sname.deleter
	def sname(self):
		del self._sname

def dog_test():
	d = Dog()
	d.fname = 'Want'			# setter of name
	print "Get Dog's name: " + d.fname 	# getter of name
	print "\n"

	d.sname = 'Wang'			# setter of nickname	
	print "Get Dog's sname: " + d.sname	# getter of nickname


if __name__ == '__main__':
	dog_test()
