# f = open("file.txt")
# lines = f.readlines()
# print(lines,type(lines))
# f.close()



#readlines also use with while loop
f = open("file.txt", "r")
line = f.readline()
while line != "":
    print(line, end="")   
    line = f.readline()

f.close()
