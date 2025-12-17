import sys


class Book:
    def __init__(self):
        self.__b = []

    def add(self):
        a = input("Enter Name of the Book\t-\t")
        if a.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)

        b = input("Enter it's author\t-\t")
        if b.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)

        c = input("Enter rent of the Book\t-\t")
        if c.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)

        try:
            c = float(c)
        except:
            print("\tInvalid Rent Amount\n\n")
            return

        z = {
            "Book Name": a,
            "Book Auther": b,
            "Book Rent": c,
            "Is book taken": False
        }
        self.__b.append(z)

    def ChooseB(self):
        if len(self.__b) == 0:
            print("\tNo Books in Library\n\n")
            return -1

        b = 1
        for a in self.__b:
            print(str(b) + "\t-\t" + a["Book Name"])
            b += 1

        a = input("Enter your Choice\t-\t")
        try:
            a = int(a)
        except:
            print("\tInvalid Choice\n\n")
            return self.ChooseB()

        if a > len(self.__b) or a <= 0:
            print("\tInvalid Choice\n\n")
            return self.ChooseB()

        return a - 1

    def get_books(self):
        return self.__b


class Member:
    def __init__(self):
        self.__m = []

    def add(self):
        a = input("Enter name of the User\t-\t")
        if a.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)

        b = input("Enter the phone Number of the User\t-\t")
        if b.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)

        try:
            b = int(b)
        except:
            print("\tInvalid Phone Number\n\n")
            return

        if len(str(b)) != 10:
            print("\tInvalid Phone Number\n\n")
            return

        c = input("Enter the amount you want to deposit in the Library Purse\t-\t")
        if c.strip().lower() == 'exit':
            print("\n\t***Exiting Program***\n\n")
            sys.exit(1)

        try:
            c = float(c)
        except:
            print("\tInvalid Amount\n\n")
            return

        z = {
            "User Name": a,
            "User Phone Number": b,
            "Amount in User's Purse": c,
            "Books rented by User": []
        }
        self.__m.append(z)

    def AnyMember(self):
        return len(self.__m) != 0

    def ChooseM(self):
        if len(self.__m) == 0:
            print("\tNo Users Registered yet\n\n")
            return -1

        b = 1
        for a in self.__m:
            print(str(b) + "\t-\t" + a["User Name"])
            b += 1

        a = input("Enter your Choice\t-\t")
        try:
            a = int(a)
        except:
            print("\tInvalid Choice\n\n")
            return self.ChooseM()

        if a > len(self.__m) or a <= 0:
            print("\tInvalid Choice\n\n")
            return self.ChooseM()

        return a - 1

    def rent(self, a, B, b):
        books = B.get_books()

        if books[b]["Is book taken"]:
            print("\tBook already rented\n\n")
            return

        books[b]["Is book taken"] = True
        self.__m[a]["Books rented by User"].append(books[b])

        print("Book Name\t-\t" + books[b]["Book Name"])
        print("Book Author\t-\t" + books[b]["Book Auther"])
        print("Book Rent\t-\t" + str(books[b]["Book Rent"]))
        print("\tBook is Successfully Rented by " + self.__m[a]["User Name"])

    def ret(self, a, B, b):
        book = self.__m[a]["Books rented by User"][b]
        book["Is book taken"] = False
        del self.__m[a]["Books rented by User"][b]
        print("\tBook Returned\n\n")

    def details(self, a):
        print("\nDetails of the User\t-\n")
        print(self.__m[a])
        print("\n\n")

    def Choose(self, a):
        if len(self.__m[a]["Books rented by User"]) == 0:
            print("\tThis user did not rent any Book yet\n\n")
            return -1

        b = 1
        for c in self.__m[a]["Books rented by User"]:
            print(str(b) + "\t-\t" + c["Book Name"])
            b += 1

        b = input("Enter your Choice\t-\t")
        try:
            b = int(b)
        except:
            print("\tInvalid Choice\n\n")
            return self.Choose(a)

        if b > len(self.__m[a]["Books rented by User"]) or b <= 0:
            print("\tInvalid Choice\n\n")
            return self.Choose(a)

        return b - 1


print("You can enter 'exit' at any moment to exit\n\n")
B = Book()
M = Member()

while True:
    print("1\t-\tRegister a new Book")
    print("2\t-\tRegister a new Member")
    print("3\t-\tLogin to a Member")
    a = input("Enter your choice {1/2/3}\t-\t")

    if a == '1':
        B.add()

    elif a == '2':
        M.add()

    elif a == '3':
        if M.AnyMember():
            print("1\t-\tRent a Book")
            print("2\t-\tReturn a Book")
            print("3\t-\tSee Details")
            b = input("Enter your Choice {1/2/3}\t-\t")

            if b == '1':
                a = M.ChooseM()
                if a == -1:
                    continue
                b = B.ChooseB()
                if b == -1:
                    continue
                M.rent(a, B, b)

            elif b == '2':
                a = M.ChooseM()
                if a == -1:
                    continue
                b = M.Choose(a)
                if b == -1:
                    continue
                M.ret(a, B, b)

            elif b == '3':
                a = M.ChooseM()
                if a == -1:
                    continue
                M.details(a)

            elif b.strip().lower() == 'exit':
                break

            else:
                print("\tInvalid Choice\n\n")
        else:
            print("\tNo User Registered yet\n\n")

    elif a.strip().lower() == 'exit':
        break

    else:
        print("\tInvalid Choice\n\n")
