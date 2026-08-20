def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=1
    return fact 
num=int(input("enter a number:"))
print("factorial:",factorial(num))