n=int(input("enter the number:"))
if n<=1:
    print("its a inavlid input {}".format(n))
else:
    for i in range(2,n+1):
        res=False
        for j in range(2,i):
            if i%j==0:
                res=True
                break
        if (res==False):
                print("\t{}".format(i))
