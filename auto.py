
class Auto:
    
    def __init__(self,mod,ear,col,pri,man,eng):
        self.model = mod
        self.ear = ear
        self.color = col
        self.price = pri
        self.manufacturer = man
        self.engine_size = eng
        
    
    def model(self,mod):
        self.model = mod
        
    def ear(self,ear):
        self.ear = ear
        
    def color(self,col):
        self.color = col
        
    def price(self,pri):
        self.price = pri
        
    def manufacturer(self,man):
        self.manufacturer = man
    
    def engine_size(self,eng):
        self.engine_size = eng
        
    def __str__(self):
        return [self.model,self.ear,self.color,self.price,self.manufacturer,self.engine_size]
    
    @property
    def wasd(self):
        return self.model,self.ear,self.color,self.price,self.manufacturer,self.engine_size
    
    
obj = Auto('porche',2016,'silver',5_000_000,'porche',2.9)

print(obj.__str__())
print(obj.wasd)
print(obj.__dict__)







