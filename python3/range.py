a = range(1, 10, 2)  # (inclusive, exclusive, step)
print(a)
print(tuple(a))
print(list(a))
print(len(a))
print(type(a))

print("-" * 40);

a2 = range(1, -21, -1)
print(list(a2))
print(len(a2))

print("-" * 40);

a3 = range(0, 11, 2)
print(list(a3))
print(sum(a3))
