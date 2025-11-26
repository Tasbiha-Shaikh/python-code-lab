s = set()
s.add(18)
s.add("18")
print(s)


s = set()
s.add(20)
s.add("20")
s.add(20.0)
print(len(s))


s = {}
print(type(s))