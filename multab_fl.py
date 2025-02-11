n=int(input("enter the number:"))
print("*"*50)
if n<=0:
    print("its a invalid")
else:
    for i in range(1,11):
        print("{} X {} = {}".format(n,i,n*i))
    else:
        print("*"*50)
