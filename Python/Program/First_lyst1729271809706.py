"""
Write a program to count 'a' in a given string.
"""
s=input("Enter a string")
count=0
for ch in s:
    if ch=='a':
        count+=1
print("Count =",count)

"""
Write a program to count a digit 9 present in the mobile number entered by the user.
"""
mobile_no=int(input("Enter your mobile number: "))
count=0

for digit in str(mobile_no):
    if digit=='9':
        count+=1
print("Count =",count)

"""
Print all the characters of a string, but stop printing if 'r' appeared in the sequence. If all the characters successfully printed then print the message - "All the characters are processed"
"""

s=input("Enter a string: ")

for ch in s:
    if ch=='r':
        break
    print(ch,end='')
else:
    print("All the characters are processed")

"""
Write a program to calculate sum of first n multiples of a given number.
"""
num=int(input("Enter a number: ")) #num=4
n=int(input("How many multiples you want to add? ")) #5
# 4+8+12+16+20=60
s=0
for x in range(1,n+1):
    s= s+num*x
print("sum is",s)