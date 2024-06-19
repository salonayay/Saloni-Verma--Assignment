n=int(input("Enter till which number you want to print series===="))
f1=0
f2=1
if (n==1):
    print(f1)
elif (n==2):
    print(f2)
else:
   print(f1,f2,end=" ")
   for i in range(3,n+1):
       f3=f1+f2
       print(f3,end=" ")
       f1=f2
       f2=f3