while (True):
    import sys
    print("*"*50)
    print("\tArthimatic operations")
    print("*"*50)
    print("\t1.Addition")
    print("\t2.Subtraction")
    print("\t3.Multiplication")
    print("\t4.Division")
    print("\t5.Modulo Division")
    print("\t6.exponention")
    print("\t7.exit")
    print("*"*50)
    ch=int(input("enter your choice:"))
    if ch<=0:
        print("-ve number is not aviable")
    elif (ch>0) and (ch<8):
        match(ch):
            case 1:
                a=float(input("enter the a val:"))
                b=float(input("enter the b val:"))
                print("sum of ({}+{})={}".format(a,b,a+b))
            case 2:
                a = float(input("enter the a val:"))
                b = float(input("enter the b val:"))
                print("sub of ({}-{})={}".format(a, b, a - b))
            case 3:
                a = float(input("enter the a val:"))
                b = float(input("enter the b val:"))
                print("mul of ({}X{})={}".format(a, b, a * b))
            case 4:
                a = float(input("enter the a val:"))
                b = float(input("enter the b val:"))
                print("div of ({}/{})={}".format(a, b, a / b))
            case 5:
                a = float(input("enter the a val:"))
                b = float(input("enter the b val:"))
                print("mod div of ({}%{})={}".format(a, b, a %b))
            case 6:
                a = float(input("enter the a val:"))
                b = float(input("enter the b val:"))
                print("sum of ({}**{})={}".format(a, b, a**b))
            case 7:
                print("thanks for using this program")
                sys.exit()
    else:
        print("enter the number within the choise")