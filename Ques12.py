n=int(input("Enter the given number="))   
sum=0
while(n>0):
    sum=sum+n%10 
    n=n//10  
print("Sum of digits =",sum)
