class details:
    _name="Tim"
    _age=35
    _job="Developer"
class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)
 
obj = pro_mod()
print("Name:",obj.name)
print("Age:",obj.age)
