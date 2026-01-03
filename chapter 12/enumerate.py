l = [2,5,6,45]

index = 0
for item in l:
    print(f"the item number at index {index} is {item}")
    index +=1

#this can simplified by enumerate function

for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")
