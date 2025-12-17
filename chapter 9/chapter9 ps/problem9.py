with open("p4.txt") as f:
    content1 = f.read()

with open("hiscore.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes, these files' contents are identical")
else:
    print("No, these files are not identical")
