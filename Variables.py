import datetime

pi = 3.5
name = "Jeff"
DOB = 1997
Age = datetime.date.today().year - DOB
output = "Hello {}. You are {} years old.".format(name, Age)


print(output)