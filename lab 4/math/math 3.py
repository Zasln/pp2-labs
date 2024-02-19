import math
n=int(input("Input number of sides: "))
a=int(input("Input the length of a side: "))
pi=math.pi
cot=1/math.tan(pi/n)
print("The area of polygon:",(n/4)*a*a*cot)