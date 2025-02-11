a=int(input("enter the num or digit:"))
if a>=0 and a<=9:
    print("{} its is a digit".format(a))
elif a>=10 and a<=20:
    print("it is a number range btw 10-20 {}".format(a))
elif a>=21 and a<=30:
    print("it is a number range btw 21-30 {}".format(a))
elif a>=31 and a<=40:
    print("it is a number range btw 31-40 {}".format(a))
elif a>=41 and a<=50:
    print("it is a number range btw 41-50 {}".format(a))
else:
    print("its is invalid number out of range 0-50")

