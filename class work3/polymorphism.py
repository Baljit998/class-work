# polymorphic functions

print(len("hello"))

print(len([10, 20, 30]))




# user defined Polymorphism
def add(x, y, z = 0):
	return x + y+z

print(add(2, 3))
print(add(2, 3, 4))


#Function polymorphism
print('')
print(len("Program"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))
