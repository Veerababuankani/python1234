line=input("enter the line of text:")
d={}
for ch in line:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
else:
    print("*"*50)
    print("given line of text{}:".format(line))
    for k,v in d.items():
        print("{}-->{}".format(k,v))