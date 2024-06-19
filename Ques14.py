lines=[]
while True:
    l=input()
    if l:
        lines.append(l)
    else:
        break
for i in lines:
    print(i,end=" ")