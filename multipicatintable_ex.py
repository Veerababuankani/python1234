ko=int(input("enter the sequence of table:"))
if ko<=0:
    print("its is invalid input{}".format(ko))
else:
    print("*"*50)
    for i in range(1,ko+1):
        if (i<=0):
            print("its a invalid")
        else:
            print(" multipulicatin tables for {}".format(i))
            for x in range(1,11):
                print("\t{} X {} = {}".format(i,x,i*x))
            else:
                print("-"*50)