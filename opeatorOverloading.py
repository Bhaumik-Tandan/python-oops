"""
Question 7: Operator Overloading
Define a class ComplexNumber to represent complex numbers. 
Implement methods to add, subtract, and multiply complex numbers using operator overloading. 
Also, provide a __str__() method to display complex numbers in a human-readable format.
"""

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

# Creating complex numbers
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

# Using operator overloading
result_add = c1 + c2
result_sub = c1 - c2
result_mul = c1 * c2
result_div = c1 / c2
equal = c1 == c2

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division: {result_div}")
print(f"Equality: {equal}")
