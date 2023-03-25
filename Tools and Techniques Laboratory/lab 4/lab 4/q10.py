tuple1 = (('a', 2), ('b', 7), ('c', 1), ('d', 9))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)
