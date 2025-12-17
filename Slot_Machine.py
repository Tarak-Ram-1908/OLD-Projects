import random
import time


print("\n\nStarting balance: ₹5000")
print("You can enter 'exit' at any moment to exit\n\n")
z = 5000


def play(z, a):
    b = random.randint(0, 999)
    for i in range(1, b+1):
        print("\r" + str(i), end="")
        time.sleep(0.01)
    print(".\t",end = "")
    c = random.randint(0, 999)
    for i in range(1, c+1):
        print("\r" + "\t\t" + str(i), end="")
        time.sleep(0.01)
    print(".\t",end = " ")
    d = random.randint(0, 999)
    for i in range(1, d+1):
        print("\r" + "\t\t\t\t" + str(i), end="")
        time.sleep(0.01)
    print(".\n")
    
    
    if((b==c)and(c==d)):
        return z + 999*a
    elif(((b%100==c%100)and(c%100==d%100))or((b/10==c/10)and(c/10==d/10))):
        return z + 99*a
    elif(((b%10 == c%10)and(c%10 == d%10))or(((b%100)/10 == (c%100)/10)and(c%10 == d%10))or((b/100 == c/100)and(c/100 == d/100))):
        return z + 9*a
    else:
        return z - a

while(1):
    if(z>0):
        print("Your Balence\t-\t"+str(z))
        print("1\t-\tPlay Again")
        print("2\t-\tDeposit Amount")
        a = input("Enter your choice\t{1/2}\t-\t")
        print()
        if(a=='1'):
            b = input("How much is your Bet\t-\t")
            print()
            if(b.strip().lower()=='exit'):
                print("\t***Exiting Program***\n\n")
                break
            try:
                b = float(b)
            except:
                print("\tInvalid Input\n")
                continue
            if(b>z):
                print("You only have " + str(z) + " in your account\n")
                continue
            else:
                z = play(z, b)
        elif(a=='2'):
            b = input("How much do you want to deposit\t-\t")
            print()
            if(b.strip().lower()=='exit'):
                print("\t***Exiting Program***\n\n")
                break
            try:
                b = float(b)
            except:
                print("\tInvalid Input\n")
                continue
            z = z+b
        elif(a.strip().lower()=='exit'):
            print("\t***Exiting Program***\n\n")
            break
        else:
            print("\tInvalid Input\n")
    else:
        print("Your Balence\t-\t"+str(z))
        a = input("Enter 1 to Deposit Amount\t-\t")
        print()
        if(a=='1'):
            b = input("How much do you want to deposit\t-\t")
            print()
            try:
                b = float(b)
            except:
                print("\tInvalid Input\n")
                continue
            z = z+b
        elif(a.strip().lower() == 'exit'):
            print("\t***Exiting Program***\n\n")
            break
        else:
            print("\tInvalid Input\n")