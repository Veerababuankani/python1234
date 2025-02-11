line=input("enter the line of text:")
print("-"*50)
print("given line of tex:{}".format(line))
print("-"*50)
words=line.split()
for word in words:
    if (len(word)%2==0):
        print("\t{}".format(word))
print("-"*50)
#for not even length of words
print("method-2")
print("-"*50)
print("given line of tex:{}".format(line))
print("-"*50)
words=line.split()
for word in words:
    if (len(word)%2!=0):
        print("\t{}".format(word))
print("-"*50)