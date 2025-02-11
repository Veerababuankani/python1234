while(True):
    import sys
    print("*" * 50)
    print("\tArea of Figures")
    print("*" * 50)
    print("\tR.Rectangle")
    print("\tC.Circle")
    print("\tS.Square")
    print("\tT.Triangle")
    print("\tE.Exit")
    print("*" * 50)
    ch=input("enter your choice:")
    match(ch.upper()):
        case 'R':
            l=float(input("enter the l :"))
            b=float(input("enter the b :"))
            print("are of rectangle={}".format(l*b))
        case 'c':
            r=float(input("enter thr r val:"))
            print("are of circle={}".format(3.14*(r**2)))
        case 'S':
            s=float(input("enter the side of square:"))
            print("are of square={}".format(s*s))
        case 'T':
            l = float(input("enter the l :"))
            b = float(input("enter the b :"))
            print("are of rectangle={}".format(0.5*l * b))
        case 'E':
            print("thanks for using this program")
            sys.exit()
        case _:
            print("u entered the wrong choice:")
