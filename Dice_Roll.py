import random

print("You should enter '0' to stop rolling the dice")
print("You should enter '1' to roll the dice\n\n")
while(1):
    a = input("0/1\t-\t")
    try:
        a = int(a)
    except:
        print("Invalid Input\n\n")
        continue
    if(a==0):
        print("\t***Exiting Program***\n\n")
        break
    elif(a==1):
        b = random.randint(1, 6)
        print("\n\t" + str(b) + "\n\n")
    else:
        print("\t***Invalid Input***\n\n")