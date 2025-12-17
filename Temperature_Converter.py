def c_k(a):
    return a+273.15
def c_f(a):
    return (a*1.8)+32
def k_c(a):
    return a-273.15
def f_c(a):
    return (a-32)/1.8

print("\n\nYou can enter 'exit' to exit any moment\n\n")
while(1):
    print("Select the Input Temperature Scale")
    print("1\t-\tCelsius")
    print("2\t-\tKelvin")
    print("3\t-\tFarenheit")
    a = input("Enter your choice (1/2/3)\t-\t")
    print("\n")

    if (a=='1'):
        c = input("Enter temperature in Celcius\t-\t")
        print("\n")
        if(c.strip().lower()=='exit'):
            print("\t***Exiting Program***\n\n")
            break
        print("Select the output Temperature Scale")
        print("1\t-\tKelvin")
        print("2\t-\tFarenheit")
        b = input("Enter your choice (1/2)\t-\t")
        print("\n")
        if(b.strip().lower()=='exit'):
            print("\t***Exiting Program***\n\n")
            break
        try:
            c = float(c)
        except:
            print("Improper TEMPERATURE Value")
            continue
        if(b=='1'):
            d = c_k(c)
            print(str(c) + "°C = " + str(d) + "K")
        elif(b=='2'):
            d = c_f(c)
            print(str(c) + "°C = " + str(d) + "°F")
        else:
            print("Invalid Choice of Temperature Scale\n\n")
        continue

    elif(a=='2'):
        c = input("Enter temperature in Kelvin\t-\t")
        print("\n")
        if(c.strip().lower()=='exit'):
            print("\t***Exiting Program***\n\n")
            break
        print("Select the output Temperature Scale")
        print("1\t-\tFarenheit")
        print("2\t-\tCelsius")
        b = input("Enter your choice (1/2)\t-\t")
        print("\n")
        if(b.strip().lower()=='exit'):
            print("\t***Exiting Program***\n\n")
            break
        try:
            c = float(c)
        except:
            print("Improper TEMPERATURE Value")
            continue
        if(b=='1'):
            d = k_c(c)
            d = c_f(d)
            print(str(c) + "K = " + str(d) + "°F")
        elif(b=='2'):
            d = k_c(c)
            print(str(c) + "K = " + str(d) + "°C")
        else:
            print("Invalid Choice of Temperature Scale\n\n")
        continue

    elif(a=='3'):
        c = input("Enter temperature in Farenheit\t-\t")
        print("\n")
        if(c.strip().lower()=='exit'):
            print("\t***Exiting Program***\n\n")
            break
        print("Select the output Temperature Scale")
        print("1\t-\tCelsius")
        print("2\t-\tKelvin")
        b = input("Enter your choice (1/2)\t-\t")
        print("\n")
        if(b.strip().lower()=='exit'):
            print("\t***Exiting Program***\n\n")
            break
        try:
            c = float(c)
        except:
            print("Improper TEMPERATURE Value")
            continue
        if(b=='1'):
            d = f_c(c)
            print(str(c) + "°F = " + str(d) + "°C")
        elif(b=='2'):
            d = f_c(c)
            d = c_k(d)
            print(str(c) + "°F = " + str(d) + "K\n\n")
        else:
            print("Invalid Choice of Temperature Scale")
        continue

    elif(a.strip().lower()=='exit'):
        print("\t***Exiting Program***\n\n")
        break

    else:
        print("Invalid Choice of Temperature Scale")
        print("\n")