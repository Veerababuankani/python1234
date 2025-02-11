n=int(input("enter the number:"))
print("*"*50)
print("method-1")
print("*"*50)
if n<=0:
    print("invalid input:")
else:
    for i in range(1,n+1):
        if n%i==0:
            print(i)
print("*"*50)
print("method-2")
print("*"*50)
if n<=0:
    print("invalid input:")
else:
    for i in range(1,n//+1):
        if n%i==0:
            print(i)
print("*"*50)