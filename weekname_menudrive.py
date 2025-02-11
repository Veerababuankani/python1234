print("*"*50)
print("\t method-2")
print("*"*50)
wkn=input("enter the name of the name:")
match(wkn.lower()):
    case "sunday":
        print("{} is holiday today".format(wkn))
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday" | "saturday":
        print("{} is workinday today".format(wkn))
    case _:
        print("{} is  not day".format(wkn))
print("*"*50)

print("\t method-1")
print("*"*50)
wkn=input("enter the name of the name:")
match(wkn.lower()):
    case "sunday":
        print("{} is holiday today".format(wkn))
    case "monday":
        print("{} is workinday today".format(wkn))
    case "tuesday":
        print("{} is workinday today".format(wkn))
    case "wednesday":
        print("{} is workinday today".format(wkn))
    case "thursday":
        print("{} is workinday today".format(wkn))
    case "friday":
        print("{} is workinday today".format(wkn))
    case "saturday":
        print("{} is workinday today".format(wkn))
    case _:
        print("{} is  not day".format(wkn))
print("*" * 50)
print("\t method-3")
print("*" * 50)
wkn=input("enter the name of the name:")
if (wkn.lower() in "monday"):
    print("{} is working day".format(wkn))
elif(wkn.lower() in "tuesday"):
    print("{} is working day".format(wkn))
elif(wkn.lower() in "wednesday"):
    print("{} is working day".format(wkn))
elif(wkn.lower() in "thursday"):
    print("{} is working day".format(wkn))
elif(wkn.lower() in "friday"):
    print("{} is working day".format(wkn))
elif(wkn.lower() in "saturday"):
    print("{} is working day".format(wkn))
elif(wkn.lower() in "sunday"):
    print("{} is holiday".format(wkn))
