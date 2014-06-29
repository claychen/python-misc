# -*- coding: utf-8 -*-

class Flower(object):
	def _get_name(self, praise):
		raise NotImplementedError('Subclasses should implement this.')

class Iris(Flower):
	def _get_name(self, praise):
		print('In Iris')
		raise NotImplementedError('subclasses should implement this.')
	def _get_owner(self):
		raise NotImplementedError('subclasses should implement this.')
	def _get_nothing(self):
		raise NotImplementedError('subclasses should implement this.')
	
class Santosa(Iris):
	def __init__(self, owner):
		self.owner = owner
	def _get_name(self, praise):
		print('Hello, this kind of flower is Santosa.\n' + praise)
	def _get_owner(self):
		print('owner is ' + self.owner)

def main():
	f = Santosa('clay')
	f._get_name('This is gorgeous')
	f._get_owner()
	#f._get_nothing()

if __name__ == '__main__':
	main()	
