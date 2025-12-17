import sys

class account:
    def __init__(self):
        self.__l = []

    def NoUser(self):
        if(len(self.__l) == 0):
            return True
        else:
            return False
    
    def ViewUsers(self):
        b = 1
        for a in self.__l:
            print(str(b) + "\t-\t" + ((self.__l)[b-1])['AHN'])
            b = b+1
        a = input("Enter the number of your USER\t-\t") 
        if(a.strip().lower() == 'exit'):
            print("\n\n\t***Exiting Program***\n\n")
            sys.exit(1)
        try:
            a = int(a)
        except:
            print("\tInvalid Choice\n\n")
            self.ViewUsers()
        if(a > len(self.__l)):
            print("\tInvalid Choice\n\n")
            self.ViewUsers()
        else:
            return a
    
    def append(self, a, b):
        c = {
            'AHN' : a,
            'A' : b
        }
        self.__l.append(c)
        print("\tUser Registered\n\n")

    def deposit(self, a, amount):
        ((self.__l)[a])['A'] = ((self.__l)[a])['A'] + amount
        print("\tAmount Credited\n\n")

    def withdraw(self, a, amount):
        ((self.__l)[a])['A'] = ((self.__l)[a])['A'] - amount
        print("\tAmount Debited\n\n")
        
    def details(self, a):
        print("\nAccount Holder Name\t-\t" + str((self.__l[a])['AHN']))
        print("Account Balence\t-\t" + str((self.__l[a])['A']) + "\n\n")





print("\n\nYou can enter 'exit' at any moment to exit\n")
obj = account()

while True:
    print("1\t-\tNew User")
    print("2\t-\tLogin to old user")
    z = input("Enter your choice {1/2}\t-\t")

    if(z == '1'):
        a = input("Enter name of the Account Holder\t-\t")
        if(a.strip().lower() == 'exit'):
            print("\n\n\t***Exiting Program***\n\n")
            break
        b = input("Enter the amount to be deposited in his Account\t-\t")
        if(b.strip().lower() == 'exit'):
            print("\n\n\t***Exiting Program***\n\n")
            break
        try:
            b = float(b)
        except:
            print("\tInvalid Amount\n\n")
            continue
        obj.append(a, b)

    elif(z == '2'):
        if(obj.NoUser()):
            print("\tNo User Registered yet\n\n")
            continue
        else:
            a = obj.ViewUsers()
            print("1\t-\tDeposit Amount")
            print("2\t-\tWithdraw Amount")
            print("3\t-\tView Details of the User")
            b = input("Enter your choice {1/2/3}\t-\t")
            if(b == '1'):
                c = input("Enter the Amount to Deposit\t-\t")
                try:
                    c = float(c)
                except:
                    print("\tInvalid Amount\n\n")
                    continue
                obj.deposit(a-1, c)
            elif(b == '2'):
                c = input("Enter the Amount to Withdraw\t-\t")
                try:
                    c = float(c)
                except:
                    print("\tInvalid Amount\n\n")
                    continue
                obj.withdraw(a-1, c)
            elif(b == '3'):
                obj.details(a-1)
            elif(b.strip().lower() == 'exit'):
                print("\n\n\t***Exiting Program***\n\n")
                break
            else:
                print("\tInvalid Input\n\n")



    elif(z.strip().lower() == 'exit'):
        print("\n\n\t***Exiting Program***\n\n")
        break

    else:
        print("\tInvalid Choice\n\n")