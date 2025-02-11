lst=int(input("enter the many tables u want:"))
if lst<=0:
    print("its a invalid input {}".format(lst))
else:
    print("*"*50)
    print("enter the {}  values for genrating mul tables".format(lst))
    print("*"*50)
    l=[]
    for i in range(1,lst+1):
        val=int(input())
        l.append(val)
    else:
        print("*"*50)
        print("list of values: {}".format(l))
        print("*"*50)
        for x in l:
            if x<=0:
                print("its a invalid input{}".format(x))
            else:
                print("*"*50)
                for i in range(1,11):
                    print("{} X {} = {}".format(x,i,x*i))
                else:
                    print("*"*50)

