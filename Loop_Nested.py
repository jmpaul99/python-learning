i=0
count = 0
while i < 5:
    j=0
    while j < 5:
        if i == j:
            print("(i,j)=({},{})".format(i,j))
            count+=1
        j+=1
    i += 1
print("printed {} lines".format(count))