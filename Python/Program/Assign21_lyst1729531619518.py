#Q1
for i in range(1,int(input("Enter a number: "))+1):
    print(i*2)

#Q2
for i in range(1,int(input("Enter a number: "))+1):
    print(i*2-1)

#Q3
for i in range(1,int(input("Enter a number: "))+1):
    print(i**2)

#Q4
for i in range(1,int(input("Enter a number: "))+1):
    print(i**3)

#Q5
print("Enter two numbers: ")
beg,end=int(input()),int(input())
if beg<2:
    beg=2
for num in range(beg,end):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)