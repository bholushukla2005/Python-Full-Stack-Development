#Q1
a=int(input("Enter a number"))
if a>99 and a<1000:
    print("%d is a three digit number"%(a))
else:
    print("%d is not a three digit number"%(a))

#Q2
a=int(input("Enter a number"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

#Q3
print("Enter values of a, b and c")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("Two real and distinct roots")
elif d==0:
    print("Two real and equal roots")
else:
    print("Two Imaginary roots")

#Q4
year=int(input("Enter year number"))

print("Leap Year" if year%400==0 or (year%100!=0 and year%4==0) else "Non Leap Year")

"""
if year%100==0:
    if year%400==0:
        print("Leap year")
    else:
        print("Non Leap Year")
else:
    if year%4==0:
        print("Leap year")
    else:
        print("Non Leap Year")
"""

#Q5
print("Enter three numbers")
a,b,c=int(input()),int(input()),int(input())

print(a if a>c else c if a>b else b if b>c else c)
    
        
"""
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
"""
