n=int(input("enter the number:"))
if (n<=1):
    print("{} is invalid input".format(n))
else:
    print("*"*50)
    assume="prime"
    for i in range(2,n):
        if n%i==0:
            assume=" not prime"
            break
    if(assume=="prime"):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))
print("*"*50)
print("method-2")
print("*" * 50)
if (n<=1):
    print("{} is invalid input".format(n))
else:
    print("*"*50)
    assume=True
    for i in range(2,n):
        if n%i==0:
            assume=False
            break
    if(assume==True):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))
print("*" * 50)