print("*"*50)
print("method for revering string:")
print("*"*50)
val=input("enter any value:")
rv=val[::-1]
print("original:",val)
print("reverse:",rv)
print("*"*50)
print("method for revering string using while loop:")
print("*"*50)
num=int(input("enter the number:"))
if num<=0:
    print("its a invalid")
else:
    rv=0
    while(num>0):
        d=num%10
        rv=rv*10+d
        num=num//10
    else:
        print(rv)