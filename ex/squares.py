squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
print("\n")

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
print("\n")

squares = [value**2 for value in range(1,11)]
print(squares)
print("\n")

cubes = [value**3 for value in range(1,101)]
print(cubes)
print("\n")
