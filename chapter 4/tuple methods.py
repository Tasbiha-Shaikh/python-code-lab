# a = (1, 234,"rohal",False,689)
# print(type(a))

# no = a.count(234)
# print(no)

t = (10,20,30,30,40,50,30,40,50)
    #(0,1 ,2, 3,  4, 5, 6, 7, 8)  indexing numbers
print(t.index(30))

#slicing
print(t[4:8])

#length
t = (10,20,30)
print(len(t))   

#check if elemnt exist
t = (10,20,30)
print(20 in t) 

#concatenation (joininh tuple)
t1 = (1,2,3)
t2 = (4,5)
print(t1 + t2)

#repetition
t = (1,2)
print(t * 3)  

#unpacking
my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)