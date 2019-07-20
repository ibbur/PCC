rivers = {
    'nile': 'egypt',
    'simms': 'usa',
    'brazos': 'usa',
    'amazon': 'brazil',
    }

print("All rivers and countries in our dictionary:")
for riv,cou in sorted(set(rivers.items())):
    if cou == "usa":
        print("\nThe " + riv.title() + " runs through the " + cou.upper() + ".")
    else:
        print("\nThe " + riv.title() + " runs through the " + cou.title() + ".")

print("\nRivers in our dictionary include:")
for riv in sorted(set(rivers.keys())):
    print("- " + riv.title())

print("\nCountries in our dictionary include:")
for cou in sorted(set(rivers.values())):
    if cou == "usa":
        print("- " + cou.upper())
    else:
        print("- " + cou.title())
