
class Person(object):

 def __init__(self, name, id):
    self.name = name
    self.id = id

 def Display(self):
    print(self.name, self.id)


emp = Person("Smith", 102) 
emp.Display()
