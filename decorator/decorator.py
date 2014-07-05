#
# use @property @xxx.setter @xxx.deleter to specify getter, 
# setter and deleter for the variable of a object
class Dog(object):
	def __init__(self):
		self._firstname = None
		self._secondname = None

	@property
	def firstname(self):
		print  "Getting Dog's name"
		return self._firstname
	@firstname.setter
	def firstname(self, value):
		print "Setting Dog's name"
		self._firstname = value
	@firstname.deleter
	def firstname(self):
		del self._firstname

	@property
	def secondname(self):
		print "Getting Dogs's name"
		return self._secondname
	@secondname.setter
	def secondname(self, value):
		print "Setting Dog's nickname"
		self._secondname = value
	@secondname.deleter
	def secondname(self):
		del self._secondname

def dog_test():
	d = Dog()
	d.firstname = 'Want'			# setter of name
	print "Get Dog's name: " + d.firstname 	# getter of name
	d.secondname = 'Wang'			# setter of nickname	
	print "Get Dog's secondname: " + d.secondname	# getter of nickname


if __name__ == '__main__':
	dog_test()
