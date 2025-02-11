#print in n natural numbers
print("="*50)
print("print in n natural numbers")
print("="*50)
n=int(input("enter the n natural number:"))
print("="*50)
if n<=0:
    print("its is a invalid input")
else:
    i=1
    x=0
    while (i<=n):
        print("natural number is = {}".format(i))
        x=x+i
        i=i+1
    else:
        print("sum of n natural number is {}".format(x))
print("*"*50)
print("print in ss of n natural numbers")
print("*"*50)
n=int(input("enter the n natural number:"))
print("*"*50)
if n<=0:
    print("its is a invalid input")
else:
    i=1
    ss=0
    while (i<=n):
        print("squares of natural number is = {}".format(i**2))
        i=i+1
        ss=ss+i**2
    else:
        print("ss of natural number is = {}".format(ss))
print("*"*50)
print("print in cs of n natural numbers")
print("*"*50)
n=int(input("enter the n natural number:"))
print("*"*50)
if n<=0:
    print("its is a invalid input")
else:
    i=1
    cs=0
    while (i<=n):
        print("cube of natural number is = {}".format(i**3))
        i=i+1
        cs=cs+i**3
    else:
        print("cs of natural number is = {}".format(cs))
print("#"*50)
print("\tsum of num is={}".format(x))
print("\tsum of sq num is={}".format(ss))
print("\tsum of cb num is={}".format(cs))
print("#"*50)