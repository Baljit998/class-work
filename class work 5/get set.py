class getset:  
   def __init__(self, age=49):  
      self._age = age  
  
   def get_age(self):  
      return self.__age   
   def set_age(self, a):  
      self.__age = a  
grad_obj = getset()  
print(grad_obj._age)  
 
print(grad_obj.get_age())  
  
grad_obj.set_age(2020)  
print(grad_obj._age)  
