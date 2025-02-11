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
#decide the grade
if c<40:
    fs1="c-fail"
else:
    fs1="c-pass"
if cpp<40:
    fs2="c++-fail"
else:
    fs2="c++-pass"
if py<40:
    fs3="python-fail"
else:
    fs3="python-pass"
#decieding grade
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
#displaying the student report
print("="*50)
print("\tdisplaying the student marks memo")
print("="*50)
print("\tstudent name:{}".format(sname))
print("\tstudent sno:{}".format(sno))
print("\t student marks in c:{}--->{}".format(c,fs1))
print("\t student marks in c++:{}--->{}".format(cpp,fs2))
print("\t student marks in Python:{}--->{}".format(py,fs3))
print("\t student totalmarks:{}".format(total_marks))
print("\t student percentage:{}".format(percentage))
print("\t student garde:{}".format(grade))
print("*"*50)