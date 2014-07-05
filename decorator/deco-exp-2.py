
class Dog(object):
	def __init__(self):
		self._fname = None
		self._sname = None

	def __getf__(self):
		print "Getting Dog's fname"
		return self._fname
	def __setf__(self, value):
		print "Setting Dog's fname"
		self._fname = value
	def __delf__(self):
		del self._fname

	f = property( __getf__, __setf__, __delf__)


	def __gets__(self):
		print "Getting Dog's sname"
		return self._sname
	def __sets__(self, value):
		print "Setting Dog's sname"
		self._sname = value
	def __dels__(self):
		del self._sname

if __name__ == '__main__':
	d = Dog()
	d.f = 'Want'
	print d.f
	
	d.s = 'Wang'
	print d.s
