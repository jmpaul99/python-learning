listItems = [1,2,3,4,5,6,7]
# without map
tempList=[]
for item in listItems:
    tempList.append(item*2)
print(tempList)
# with map multiply by 2
tempList2 = list(map(lambda x:x*2, listItems))
print(tempList2)
# with mapp add 3
tempList3 = list(map(lambda x:x+3, listItems))
print(tempList3)