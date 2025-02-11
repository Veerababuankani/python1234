print("="*50)
n=int(input("enter the number:"))
if n<=0:
    print("its a invalid input:")
else:
    print("=" * 50)
    s,ss,cs=0,0,0
    for i in range(1,n+1):
        print("\t\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("="*50)
        print("\t\t{}\t\t{}\t\t{}".format(s,ss,cs))
        print("=" * 50)