person=dict(Name="Jeff", Age=27, Salary=1000000)
print(person)
print(person["Name"])
person["Name"] = "Hussein"
print(person["Name"])
person["Insurance"] = "Yes"
print(person)
del person["Age"]
print(person)
