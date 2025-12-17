import random

y = 0
z = 0

while(1):
    print("\n\nYou can enter 'exit' to Exit the program\n\n")
    a = random.randint(1, 100)
    a = a%3
    print("0\t-\tRock")
    print("1\t-\tPaper")
    print("2\t-\tScissors")
    b = input("Enter your Choice\t-\t")
    if(b.strip().lower() == 'exit'):
        print("Exiting Program\n\n")
        break
    try:
        b = int(b)
    except:
        print("Invalid Input\n\n")
        continue
    if((b<0)or(b>2)):
        print("Invalid Input\n\n")
        continue

    if(a==0):
        print("Systems choice\t-\tRock")
    if(a==1):
        print("Systems choice\t-\tPaper")
    if(a==2):
        print("Systems choice\t-\tScissors")

    if((a==0)and(b==1)):
        print("You Win\n\n")
        y = y+1
        continue
    elif((a==0)and(b==2)):
        print("You Lose\n\n")
        z = z+1
        continue
    elif((a==1)and(b==0)):
        print("You Lose\n\n")
        z = z+1
        continue
    elif((a==1)and(b==2)):
        print("You Win\n\n")
        y = y+1 
        continue
    elif((a==2)and(b==0)):
        print("You Win\n\n")
        y = y+1
        continue
    elif((a==2)and(b==1)):
        print("You Lose\n\n")
        z = z+1
        continue
    else:
        print("\tDRAW\n\n")
        continue

print("\nYour Score\t-\t" + str(y))
print("\nSystem's Score\t-\t" + str(z))