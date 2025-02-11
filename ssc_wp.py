n=int(input('enter the natural number sum u wnt to find :'))
if n<=0:
    print("its a invalid input:")
else:
    i=1
    s=0
    ss=0
    cs=0
    print("=" * 50)
    print("\ts\tss\tcs")
    print("=" * 50)
    while i<=n:
        print("\t{}\t{}\t{}".format(i,i**2,i**3))
        i=i+1
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("="*50)
        print("\t{}\t{}\t{}".format(s,ss,cs))
        print("=" * 50)

