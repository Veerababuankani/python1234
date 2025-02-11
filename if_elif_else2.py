d=int(input("enter the any digit:"))
if (d==0):
    print("{} its a zero".format(d))
else:
    if (d == 1):
        print("{} its a one".format(d))
    else:
        if (d == 2):
            print("{} its a two".format(d))
        else:
            if (d == 3):
                print("{} its a three".format(d))
            else:
                if (d == 4):
                    print("{} its a four".format(d))
                else:
                    if (d == 5):
                        print("{} its a five".format(d))
                    else:
                        if (d == 6):
                            print("{} its a six".format(d))
                        else:
                            if (d == 7):
                                print("{} its a seven".format(d))
                            else:
                                if (d == 8):
                                    print("{} its a eight".format(d))
                                else:
                                    if (d == 9):
                                        print("{} its a nine".format(d))
                                    else:
                                        print(" {} is not a digit--->plz try again".format(d))

#method_2
print("-"*80)
print("\t\tmethod-2")
print("-"*80)
if (d==0):
    print("{} its a zero".format(d))
elif (d==1):
    print("{} its a one".format(d))
elif (d==2):
    print("{} its a two".format(d))
elif (d==3):
    print("{} its a three".format(d))
elif (d==4):
    print("{} its a four".format(d))
elif (d==5):
    print("{} its a five".format(d))
elif (d==6):
    print("{} its a six".format(d))
elif (d==7):
    print("{} its a seveen".format(d))
elif (d==8):
    print("{} its a eight".format(d))
elif (d==9):
    print("{} its a nine".format(d))
else:
    print("{} its not a digit".format(d))
#method_3
print("-"*80)
print("\t\tmethod-3 by using dict")
print("-"*80)
d1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
dig=int(input("enter the digit:"))
v=d1.get(dig)
if (v!=None):
    print("{} is {}".format(dig,v))
else:
    print("it is a num")
print("-"*80)
print("\t\tmethod-4 by using dict")
print("-"*80)
d1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
dig=int(input("enter the digit:"))
res=d1.get(dig) if d1.get(dig)!=None else "its a number"
print("{} is {}".format(dig,res))


