# Aaron Frankel 2019-7-17
# The purpose of this file is to learn about dictionaries.
# In a previous lesson we worked with a dictionary with info about one 'thing'.
# In this lesson we'll make a dictionary about several 'things' that a similar.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['jen','sarah','barron','maggie','daisy']

print("\nSarah's favorite language is " +
    favorite_languages['sarah'].title() + "." )

for name, language in favorite_languages.items():
    print("\n" + str(name).title() + "'s favorite language is " +
    str(language).title() + "!")

friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys()):
    print("\n" + name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll.")


print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Using a set to remove repetition
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Using a set to remove repetition AND sorting
print("\nThe following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())

# Using a list and a dictionary in tandom
print("\nMessage people about the poll.")
for name in people:
    if name in favorite_languages.keys():
        print("\nThank you for taking the poll, " + name.title() + ".")
    else:
        print("\nYou should take our poll, " + name.title() + ".")

# Added per page 112 of PCC

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in sorted(favorite_languages.items()):
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t- " + language.title())

for name, languages in sorted(favorite_languages.items()):
    if len(languages) <= 1:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t- " + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t- " + language.title())


dog_0 = {
    'name': 'barron',
    'species': 'dog',
    'breed': 'weimerener',
    'sex': 'male',
    'color': 'grey',
    }
dog_1 = {
    'name': 'maggie',
    'species': 'dog',
    'breed': 'weimerener',
    'sex': 'female',
    'color': 'blue'
}
dog_2 = {
    'name': 'daisy',
    'species': 'dog',
    'breed': 'weimerener',
    'sex': 'female',
    'color': 'blue'
}

pets = [dog_0,dog_1,dog_2]

for pet in pets:
    print(pet)


dog_spots = {
    'barron': ['lazy boy','couch','under the coffee table'],
    'maggie': ['her bed', 'my feet', 'the sofa'],
    'daisy': ['the sofa', 'under the coffee table', 'our bed'],
}

for pet, places in sorted(dog_spots.items()):
    print(pet.title() + "'s favorite places are:")
    for place in places:
        print("\t- " + place.title())

favorite_numbers = {
    'jen': [7,5,10],
    'sarah': [2,5,11],
    'edward': [3,9,24],
    'phil': [5,15,20],
    }

for name, numbers in sorted(favorite_numbers.items()):
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t -" + str(number))

cities = {
    'houston': {
        'country': 'usa',
        'population': '2.5M',
        'fact': 'high humidity',
    },
    'dallas': {
        'country': 'usa',
        'population': '1.34M',
        'fact': 'uptight',
    },
    'austin': {
        'country': 'usa',
        'population': '950K',
        'fact': 'dirty with CA transplants',
    },
}
# Add to nested dictionary piece by piece
cities['san antonio'] = {}
cities['san antonio']['country'] = 'usa'
cities['san antonio']['population'] = '1.5M'
cities['san antonio']['fact'] = 'boring'

# Add to nested dictionary with one line
cities['amarillo'] = {'country': 'usa', 'population': '200K', 'fact': 'dry'}

for k_cities,v_cities in sorted(cities.items()):
    print("\nInformation about " + k_cities.title() + ":")
    for city, information in v_cities.items():
        if information == 'usa':
            print("\t -" + information.upper())
        else:
            print("\t -" + information)

# Messing around

like = ['austin', 'houston']

for c_name in cities.keys():
    if c_name in like:
        print("\nWe like " + c_name.title() + ".")
    else:
        print("\nWe're meh about " + c_name.title() + ".")
