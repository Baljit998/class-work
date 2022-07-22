class pub_mod:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
 
    def Age(self):  
        print("Age: ", self.age)
obj = pub_mod("tim", 30);
print("Name: ", obj.name)   
obj.Age()
