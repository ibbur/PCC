# Aaron Frankel 2019-7-3

for values in range(1,21):
    print(values)

print("\n")

mill = list(range(1,1001))
for values in mill:
    print(values)

print("\n")

print(min(mill))
print(max(mill))
print(sum(mill))

print("\n")

odd = list(range(1,21,2))
for values in odd:
    print(values)

print("\n")

three = list(range(3,31,3))
for values in three:
    print(values)

print("\n")

cubes = [values**3 for values in range(1,11)]
print(cubes)
