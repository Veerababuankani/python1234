ls1=[10,20,30,-12,23,-89,23,-345,-34,54,-98]
print("+ve numbers")
for i in ls1:
    if i<=0:
        continue
    print(i)
print("*"*50)
for j in ls1:
    if j>=0:
        continue
    print(j)