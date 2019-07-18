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
