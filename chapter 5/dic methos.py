a = {
    "name":"harry",
    "from":"india",
    "marks":[23,67,90]

}

print(a.items())
print(a.keys())
print(a.get("name"))

a.update({"name": "ali"})
print(a)