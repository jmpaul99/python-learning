import datetime

dob = input("Enter your DOB:")
CurrentYear = datetime.datetime.now().year
Age = CurrentYear-int(dob)
print("Your age is {}".format(Age))
