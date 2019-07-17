# Aaron Frankel 2019-7-16
# The purpose of this file is to work with if, if-else, and if-elif-else

fruit = ['figs', 'strawberries', 'blue berries', 'banannas', 'cherries']

if 'figs' in fruit:
    print("\nI like " + fruit[0] + "!")
if 'strawberries' in fruit:
    print("\nI like " + fruit[1] + "!")
if 'blue berries' in fruit:
    print("\nI like " + fruit[2] + "!")
if 'banannas' in fruit:
    print("\nI like " + fruit[3] + "!")
if 'cherries' in fruit:
    print("\nI like " + fruit[4] + "!")


if 'apples' in fruit:
    print("\nApples are ok.")
else:
    print("\nI really like " + fruit[0] + "!")

if 'apples' in fruit:
    print("\nApples are ok.")
elif 'strawberries':
    print("\nI like " + fruit[1] + "!")
else:
    print("\n" + fruit[3] + " are decent. Best in smootheis.")
