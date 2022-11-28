a = 10 
b = 1.3256

print(a,b)
print(type(b))

class Person:
    _age:int = 1
    _name:str = 'x'
    def age(self, name):
        self._age = 10
        self._name = name

    
p  = Person()
p.age(name='ham')

print(p._name,p._age)