# Aaron Frankel 2019-7-17
# The purpose of this file is to practise building and using dictionaries.

jen = {
    'first_name': 'jennifer',
    'last_name': 'tran',
    'age': 35,
    'city': 'houston'
    }

print(jen)
print(jen['first_name'].title())
print(jen['last_name'].title())
print(jen['age'])
print(jen['city'].title())

print("\n")
for k,v in jen.items():
    print(str(v).title())

numbers = {
    'jen': 7,
    'aaron': 13,
    'barron': 12,
    'maggie': 11,
    'daisy': 10,
    }

for k,v in numbers.items():
    print("\n" + str(k).title() + "'s favorite number is " + str(v) + ".")

glossary = {
    'dictionary': 'A dictionary in Python is a collection of key-value pairs.',
    'key-value pair': 'A key-value pair is a set of values associated with each other.',
    'string': 'A string in Python is a sequence of characters.',
    }

for k,v in glossary.items():
    print("\n" + str(k).title() + ": " + str(v))
