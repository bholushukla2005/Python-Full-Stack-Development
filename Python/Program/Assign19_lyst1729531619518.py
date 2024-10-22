#Q1
s=input("Enter a string:  ")
for ch in s:
    print(ch,ord(ch))

#Q2
s=input("Enter a string:  ")
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch)

#Q3
s=input("Enter a string:  ")
count=0
for ch in s:
    if ch == ' ':
        count+=1
print("Count =",count)

#Q4
s=input("Enter a number:  ") #s='123234'
u=''
for ch in s:
    if ch not in u:
        u+=ch  
print(u)

#Q5
n=int(input("Enter a number: "))
count=0
for ch in str(n):
    if ch in "0123456789":
        count+=1
print(count)
