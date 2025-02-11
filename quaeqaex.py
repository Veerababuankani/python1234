a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a<=0 or b<=0 or c<=0:
    print("its a invalid input")
else:
    print("{}x**2+{}x+{}=0".format(a,b,c))
    r1=(0-b+(0.5*((b**2)-4*a*c)))/(2*a)
    r2=(0-b-(0.5*((b**2)-4*a*c)))/(2*a)
    print(r1,r2)