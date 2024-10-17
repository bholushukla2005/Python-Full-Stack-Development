#Q1
print("positive" if int(input("Enter a number"))>0 else "non positive")

#Q2
a=int(input("Enter a number"))

if a%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#Q3
a=int(input("Enter a number"))

if a%2==0:
    print("Even",a)
else:
    print("Odd",a)

#Q4
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(a if a>b else b)


#Q5
w1=input("Enter first word")
w2=input("Enter second word")
if(w1<w2):
    print(w1,w2)
else:
    print(w2,w1)
