a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a Tuple")

data = 1, 2, 76     # data represents a tuple
x, y, z = data      # you can't have a tuple on the left of an assignment because tuples are immutable
print(x)
print(y)
print(z)

print("Unpacking a List")

data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)
