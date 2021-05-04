import datetime

dob = input("Enter your DOB:")
CurrentYear = datetime.datetime.now().year
Age = CurrentYear - int(dob)
if Age >= 18:
    print("Your age is {} and you are an adult".format(Age))
if Age < 18:
    print("Your age is {} and you are not an adult".format(Age))
