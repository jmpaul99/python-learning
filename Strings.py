from django.template.defaultfilters import upper, lower

name = "Jeff Paulin"

print(len(name))
print(upper(name))
print(lower(name))
title = "Your grade is {}".format(79)
print(title)
str = "San Francisco{}"
str2 = " is good"
print(str.format(str2))