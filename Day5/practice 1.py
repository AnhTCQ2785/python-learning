a = (1,2,3)
b = a
c = (1,3,5)

print(id(a) == id(b))
print(id(c) == id(a))

print(a is b)
print(c is a)

