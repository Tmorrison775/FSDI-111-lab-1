
def say_hello():
    print("Hello from a method")

def sum(op1, op2):
    return op1 + op2

def menu():
    print("-" * 30)
    print("          Menu  ")
    print("[1] - Add")
    print("[2] - Subtract")
    print("[3] - Multiply")
    print("[4] - Divide")
    print("[x] - Exit")
    print("-" * 30)

print(' Wlecome to PyCalc')





opc = ""

while(opc != "X"):


    menu()
    opc = input("Select and option:")
    if(opc == "X"):
        break

    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    if(opc == '1'):
        sum_res = sum(num1, num2)
        print(str(num1) + " plus " + str(num2) + " is equal to: " + str(sum_res))
    elif (opc == '2'):
        subtract_res = num1 - num2
        print(str(num1) + " minus " + str(num2) + " is equal to: " + str(subtract_res))
    elif (opc == '3'):
        multiply_res = num1 * num2
        print(str(num1) + " multiplied by " + str(num2) + " is equal to: " + str(multiply_res))
    elif (opc =='4'):
        divide_res = num1 / num2
        print(str(num1) + " divided by " + str(num2) + " is equal to: " + str(divide_res))