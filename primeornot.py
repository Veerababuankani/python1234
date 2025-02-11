p=int(input("prime are not:"))
if p<=0:
    print("invalid input:{}".format(p))
else:
    res=False
    for i in range (2,p):
        if p%i==0:
            res=True
            break
if(res==False):
    print("its a prime number",format(p))
else:
    print("its not a prime number{}".format(p))

