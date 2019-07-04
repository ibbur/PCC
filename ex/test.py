twenty = [value for value in range(1,21)]
print(twenty)
print("\n")

million = [value for value in range(1,101)]
print(million)
print("\n")

print(min(million))
print(max(million))
print(sum(million))
print("\n")

odd_numbers = []
for value in range(0,21,2):
    odd_numbers.append(value)
    print(value)

print("\n")
for value in range(3,31,3):
    print(value)

print("\n")

for cube in range(1,11,):
    print(cube**3)

print("\n")

cube_list = [cube**3 for cube in range(1,11)]
print(cube_list)
