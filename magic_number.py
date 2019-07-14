# Aaron Frankel 2019-7-6
# The purpose of this file is to practise working with inequality checks on
# numberical comparisons

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)

print(age <= 21)

print(age > 21)

print(age >= 21)

print("\n")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

print("\n")
age_1 = 22
print(age_0 >= 21) and (age_1 >= 21)
