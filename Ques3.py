n1=int(input("Enter number whose factorial you want to find"))
fact=1
while n1>0:
    fact=fact*n1
    n1=n1-1
print("Factorial of the number is",fact)