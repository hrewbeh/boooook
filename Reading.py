

class Book:
    
    def __init__(self):
        self.name = 'name'
        self.ear = ''
        self.manufacturer = ''
        self.genre = ''
        self.author = ''
        self.price = '1001'
        
    def name(self,name):
        self.name = name
            
    def ear(self,ear):
        self.ear = ear
            
    def manufack(self,man):
        self.manufacturer = man
        
    def genre(self,gen):
        self.genre = gen
        
    def autor(self,au):
        self.author = au
    
    def price(self,pri):
        self.price = pri
            
class Read(Book):
    
    def __init__(self):
        Book.__init__(self)

    def get_all(self):
        return self.name,self.ear,self.manufacturer,self.genre,self.author,self.price
    
ret = Read()

print(ret.price)
print(ret.__dict__)