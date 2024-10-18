chance=1
while chance<=3:
    a=int(input("Enter an even number"))
    if a%2==0:
        print("You Win")
        break
    chance+=1
else:
    print("Game Over")

