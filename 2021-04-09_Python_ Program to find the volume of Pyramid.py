#2021-04-09_Python_ Program to find the volume of Pyramid
#Computer Programming Tutor_April8,2021

# Volume of a pyramid
# Functions to Calculate Volume of triangular Pyramid
def volTriangular(a,b,h):
    return (0.1666)*a*b*h
# Functions To Calculate Volume of Square Pyramid

def volSquare(b,h):
    return (0.33)*b*b*h
# Functions To Calculate Volume of Pentagonal Pyramid
def volPentagonal(a,b,h):
    return (0.83)*a*b*h
#Functions to Calculate Volume Hexagonal Pyramid
def volHexagonal(a,b,h):
    return a*b*h

b = float(input("Enter Base b:"))
h = float(input("Enter the Height h:"))
a = float(input("Enter the Value of a:"))

print("Volume of Triangular Base Pyramid",
      volTriangular(a,b,h))
print("Volume of Square Base Pyramid is : ",
    volSquare(b,h))

print("Volume of Pentagonal Base Pyramid is : ",
    volPentagonal(a,b,h))
print("Volume of hexagonal Base Pyramid is : ",
    volHexagonal(a,b,h))



