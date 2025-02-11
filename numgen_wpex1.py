n=int(input("enter the number:"))
if n<0:
    print("no -ve numbers are generaterd")
else:
    i=0
    while(i<=n):
        print(i)
        i=i+1
    else:
        print("program execution completed")
print("*"*50)
print("method-2")
print("*"*50)
n=int(input("enter the number:"))
if n<0:
    print("no -ve numbers are generaterd")
else:
    i=n
    while(i>=0):
        print(i)
        i=i-1
    else:
        print("program execution completed")