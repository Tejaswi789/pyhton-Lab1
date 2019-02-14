print("python class students")
a = [x for x in input().split()]
print("web class students")
b = [y for y in input().split()]
print("common students")
common =set(a)&set(b)
print(common)
print("noncommon students")
noncommon=set(a)^set(b)
print(noncommon)