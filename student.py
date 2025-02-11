#validation for student  sno
print("*"*50)
sname =input("enter the student name:")
while(True):
    sno = int(input("enter the student number:"))
    if sno>=100 and sno<=200:
        break
    else:
        print("u entered wrong id--->tryagain")
#marks validation for c
while(True):
    c= int(input("enter the student marks in c lang:"))
    if c>=0 and c<=100:
        break
    else:
        print("u entered wrong marks--->tryagain")
#marks validation for cpp
while(True):
    cpp= int(input("enter the student marks in cpp lang:"))
    if cpp>=0 and cpp<=100:
        break
    else:
        print("u entered wrong marks--->tryagain")
#marks validation for cpp
while(True):
    py= int(input("enter the student marks in python lang:"))
    if py>=0 and py<=100:
        break
    else:
        print("u entered wrong marks--->tryagain")
print("*"*50)
#calcuation totalmarks
total_marks=c+cpp+py
percentage=(total_marks/300)*100
#student pass or fail
if (c<40)or(cpp<40)or(py<40):
    grade="fail"
else:
    if total_marks<=300 and total_marks>=250:
        grade="distiction"
    elif total_marks<=249 and total_marks>=200:
        grade="first"
    elif total_marks<=199 and total_marks>=150:
        grade="secound"
    elif  total_marks<=149 and total_marks>=120:
        grade="third"
#displaying the student marks report
print("="*50)
print("\t student markes report")
print("="*50)
print("\tstudent name:{}".format(sname))
print("\tstudent number:{}".format(sno))
print("\tstudent marks in c lang:{}".format(c))
print("\tstudent marks in cpp lang:{}".format(cpp))
print("\tstudent marks in python lang:{}".format(py))
print("\tstudent total marks:{}".format(total_marks))
print("\tstudent percentage of marks:{}".format(percentage))
print("\tstudent grade:{}".format(grade))
print("="*50)