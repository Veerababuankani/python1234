#palindrome in single word
print("="*100)
print("method-1")
print("="*100)
word=input("enter the word:")
res="palindrome" if word==word[::-1] else "it is not palindrome"
print('{} is {}'.format(word,res))
print("="*100)
#method-2
print("method-2")
print("="*100)
res="palindrome" if word.lower()==word[::-1].lower() else "it is not palindrome"
print('{} is {}'.format(word,res))
print("="*100)
# for digit palindrome or not
print("\t method-3 for palindrome for digits")
print("="*100)
d=int(input("enter the number:"))
sno=str(d)
res="palindrome" if sno==sno[::-1] else "it is not palindrome"
print("{} is {}".format(d,res))
print("="*100)
print("##@##"*10)
print("method-4 for checking last and first char is same are not")
print("*"*50)
s=input("enter the name or word:")
res="same" if s[0]==s[-1] else "not same"
print("{}--->{}".format(s,res))
print("*"*50)

