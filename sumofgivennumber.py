n=int(input("enter the number:"))
if n<=0:
    print("its a invalid")
else:
    s=0
    while(n>0):
        d=n%10
        s=s+d
        n=n//10
    else:
        print(s)