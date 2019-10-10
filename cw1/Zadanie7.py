thislist = []

for i in range(10):
    thislist.append(i+1)

print(thislist)

thislist2 = thislist[5:10]
thislist = thislist[0:5]

thislist = thislist + thislist2
thislist.insert(0,0)
print(thislist)