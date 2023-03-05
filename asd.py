class Parent:
    def __init__(self):
        self.parent_attribute = 'name'
	    
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

child = Child()

print(child.parent_attribute)


class Book:
	
	def __init__(self):
		self.name = 'name'
		self.ear = ''
		self.manufacturer = ''
		self.genre = ''
		self.author = ''
		self.price = ''


class Read(Book):
	
	def __init__(self):
		Book.__init__(self)


ret = Read()

print(ret.name)