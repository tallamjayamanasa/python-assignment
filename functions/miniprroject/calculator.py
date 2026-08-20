def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "cannot be zero"
    return a/b
def mod(a,b):
    if b==0:
        return "cannot be zero"
    return a%b
while True:
    print("\n -----choice-----")
    print("1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")
    print("6.exit")

    choice =int(input("enter choice:"))
    if choice == 6:
        print("thank you !")
        break

    a=float(input("enter frist number"))
    b=float(input("enter second number"))

    if choice == 1:
        print("result:",add(a,b))
    elif choice== 2:
        print("result:",sub(a,b))
    elif choice== 3:
        print("result:",mul(a,b))
    elif choice == 4:
        print("result:",div(a,b))
    elif choice == 5:
        print("result:", mod(a,b))
    else :
        print("invalid choice " )