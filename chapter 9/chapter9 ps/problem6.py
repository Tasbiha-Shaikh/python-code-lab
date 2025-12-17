with open("log.txt.html","r") as f:
    content = f.read()
if("python" in content):
    print("yes python is present")

else:
    print("python is not present")