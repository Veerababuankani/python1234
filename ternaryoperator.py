#method-1
#finding the biggest number btm a and b
print("="*100)
print("\tmethod-1")
print("="*100)
a=float(input("enter the number:"))
b=float(input("enter the number:"))
c=float(input("enter the number:"))
big=a if (a>b) else b
print("the biggest number between ({},{}) ={}".format(a,b,big))
print("="*100)
#method-2
print("\tmethod-2")
print("="*100)
res=a if (a>b) else b if (a<b) else "both are eaqual"
print("the biggest number between({},{})={}".format(a,b,res))
print("="*100)
#method-3
print("\tmethod-3")
print("="*100)
res1=a if (a>b) and (a>c) else b if (b>a) and (b>c) else c if (c>a)and(c>b) else "all are eaqual"
print("large({},{},{})={}".format(a,b,c,res1))
print("="*100)
#method-4 for printing the small amog them
print("\tmethod-4")
print("="*100)
res2=a if (a<b) and (a<c) else b if (b<a) and (b<c) else c if (c<a)and(c<b) else "all are eaqual"
print(" small({},{},{})={}".format(a,b,c,res2))
print("="*100)
print("\tmethod-5")
bv=a if (b<a>c) else b if (a<b>c) else c if (a<c>b) else "all are eaqual"
print(" large({},{},{})={}".format(a,b,c,bv))
sv=a if (b>a<c) else b if (a>b<c) else c if (a>c<b) else "all are eaqual"
print(" small({},{},{})={}".format(a,b,c,sv))
print("="*100)
