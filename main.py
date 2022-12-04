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
name = input('Yyour name: ')
if name =='':
    print('You didnt enter anything')
else:

    p.age(name)
    print(p._name,p._age)

