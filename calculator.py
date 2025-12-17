import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board(expression="", result=""):
    clear_screen()
    print(" " * 20 + "-" * 30)
    print(" " * 20 + "|{:^28}|".format(" CALCULATOR "))
    print(" " * 20 + "-" * 30)
    print(" " * 20 + "|{:^28}|".format(expression))
    print(" " * 20 + "|" + " " * 28 + "|")
    print(" " * 20 + "|{:^28}|".format(result))
    print(" " * 20 + "-" * 30)

def calculate(expr):
    try:
        result = eval(expr)
        return str(result)
    except ZeroDivisionError:
        return "Error: Division by Zero"
    except:
        return "Invalid Expression"

def main():
    expression = ""
    result = ""
    
    while True:
        draw_board(expression, result)
        expression = input("\nEnter expression (or type 'exit'): ")
        
        if expression.lower() == "exit":
            draw_board("Goodbye!", "")
            break
        
        result = calculate(expression)

if __name__ == "__main__":
    main()