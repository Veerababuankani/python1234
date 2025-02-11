l1=[12,23,34,1,23,-34,-9,-33,12,-34,-987]
for n in l1:
    if(n<=0):
        print("it is a invalid input:")
    else:
        print("*"*50)
        for i in range(1,11):
            print("{} X {} = {}".format(n,i,n*i))
        print("*"*50)
print("*"*50)
print("\tmethod-2")
print("*"*50)
