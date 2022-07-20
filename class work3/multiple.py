#parent class 1
class A:
    demo1=0
    def fun1(self):
        print(self.demo1)

#parent class 2
class B:
    demo2=0
    def fun2(self):
        print(self.demo2)

#child class
class C(A, B):
    def fun3(self):
        print('Hey there, you are in the child class')

# Main code
c = C()
c.demo1 = 10
c.demo2 = 5
c.fun3()
print('first number is : ',c.demo1)
print('second number is : ',c.demo2)
