mylist = [1,7,8,9,4,3,5]

squaredlist = []
for item in mylist:
    squaredlist.append(item*item)

# simplified by list comprehensive
squaredlist = [i*i for i in mylist]
print(squaredlist)