print("="*50)
print("method for checkng palindrome or not in str")
print("="*50)
s=input("enter the word:")
if s==s[::-1]:
    print("its a palindrome")
else:
    print("its not a palindrome")
print("="*50)
print("method for checkng palindrome or not in numbers")
print("="*50)
n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    temp=n
    rv=0
    while (n>0):
        d=n%10
        rv=rv*10+d
        n=n//10
    else:
        if rv==temp:
            print("its a palindrome:")
        else:
            print("its not a palindrome:")
print("="*50)