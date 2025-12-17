word = "donkey"

with open("p4.txt","r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("p4.txt","w") as f:
     f.write(contentNew)