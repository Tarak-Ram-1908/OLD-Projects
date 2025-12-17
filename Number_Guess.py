import random

print("\n\nYou can enter 'exit' at any moment to exit")
print("I have chosen a number between 1 and 100 — try to guess it!\n\n")

z = random.randint(1, 100)

while(1):
    a = input("Enter your guess\t-\t")
    if(a.strip().lower() == 'exit'):
        print("Exiting Program\n\n")
        break
    try:
        a = int(a)
    except:
        print("INVALID GUESS\n")
        continue
    if(z > a):
        print("Too low — guess higher\n")
        continue
    elif(z < a):
        print("Too high — guess lower\n")
        continue
    else:
        print("\n\t***GOT IT***\n\n")
        break