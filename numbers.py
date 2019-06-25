# Aaron Frankel 2019-6-25
# The purpose of this file is to learn about the range() function

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

print("\n")

even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n")

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# More concisely written

squares = []
for value in range(1,50):
    squares.append(value**2)

print(squares)

print("\n")
print(min(squares))
print(max(squares))
print(sum(squares))

print("\n")

# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
squares = [value**2 for value in range(1,11)]
print(squares)
