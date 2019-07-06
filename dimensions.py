# Aaron Frankel 2019-7-5
# The purpose of this file for learing about tuples.

dimensions = (200,50)

print(dimensions[0])
print(dimensions[1])

print("\n")

print("Original deimensions:")
for dimension in dimensions:
    print(dimension)

print("\n")

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print("\n")

When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that should not be changed throughout th elife of a program.
