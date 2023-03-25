# 1).  Define a class complex with required attributes and member functions. and two complex number and display the result  
 #   ex :-
#          enter the complex matrix 1: 2+3j
#          enter the complex matrix 2: 4+5j
#          ---------------------------------
#          complex after addition : 6+8j

class complex:
    def __init__(self, real, imag): # constructor __init__ is used to initialize the attributes of the class
        self.real = real
        self.imag = imag

    def __add__(self, other): # __add__ is used to add two complex numbers
        return complex(self.real+other.real, self.imag+other.imag)

    def __str__(self): # __str__ is used to print the complex number in the form of (a+bi)
        return "({}+{}i)".format(self.real, self.imag)


c1 = complex(int(input('Real part of 1st complex number: ')), int(input('Imaginary part of 1st complex number: ')))
c2 = complex(int(input('Real part of 2nd complex number: ')), int(input('Imaginary part of 2nd complex number: ')))
c3 = c1+c2
print(f'Sum of {c1} and {c2} is {c3}')