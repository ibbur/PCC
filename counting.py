# Aaron Frankel 2019-6-26
# The purpose of this file is to practise working with lists and numbers

squares = [value**2 for value in range(1,11)]
print(squares)

for value in range(1,21):
    print(value)

for value in range(22,41):
    print(value)

for value in range(41,61):
    print(value)

for value in range(1,10001):
    print(value)

minmax = list(range(1,10001))
print(min(minmax))
print(max(minmax))

print("\n")

even_numbers = list(range(2,21,2))
print(even_numbers)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n___ Continue ___")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
