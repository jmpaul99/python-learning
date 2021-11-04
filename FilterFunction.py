listItems = [1,2,3,4,5,6,7,8,9,10]
print(listItems)
# without filters
templist=[]
for item in listItems:
    if (item % 2==0):
        templist.append(item)
print(templist)
# with filter
templist2=list(filter(lambda x: x%2==0,listItems))
print(templist2)