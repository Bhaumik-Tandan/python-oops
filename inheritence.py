"""
Question 6: Multiple Inheritance
Create a class A with a method foo(). 
Design classes B and C that inherit from A. Now create a class D that inherits from both B and C. 
Implement a method bar() in class D that calls foo() from both B and C.
"""

class A:
    def foo(self):
        print(f"Foo called from {type(self).__name__}")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    def bar(self):
        B.foo(self)
        C.foo(self)

d=D()
d.bar()
