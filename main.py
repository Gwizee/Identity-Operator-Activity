x = 20

if (type(x) is int) :
    print("True,x is an integer")
else :
    print("False,x is not an integer")

y = 10.0

if (type(y) is float) :
    print("True,y is a float")
else :
    print("False,y is not a float")

a = 40
b = 40

if (a is b) :
    print("Same indentity")
else :
    print("Different identity")

b = 50

if (a is not b) :
    print("Different identity")
else :
    print("same indentity")
