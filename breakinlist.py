#breakinloops
print("*"*50)
print("method-1")
print("*"*50)
l1=[10,20,30,40,50,60,70,80,90]
for v in l1:
    if v==60:
        break
    else:
        print(v)
else:
    print("*"*50)