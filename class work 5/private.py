class Person:
    def __init__(self, name, age, height):
        self.name     = name   # public
        self._age     = age    # protected
        self.__height = height # private

p1 = Person("Tim", 20, 17)

print(p1.name)        
print(p1._age)        
# print(p1.__height)  
