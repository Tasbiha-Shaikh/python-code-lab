words = ["donkey","bad","good","gande"]

with open("p4.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open("p4.txt","w") as f:
     f.write(content)