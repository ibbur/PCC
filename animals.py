# Aaron Frankel 2019-6-25
# The purpose of this file is to exercise my use of the for loop

animals = ['squirrels', 'weimaraners', 'otters']
for animal in animals:
    print(animal)
for animal in animals:
    print("\n" + animal.title() + " are very silly creatures.")

print("\n" + animals[0].title() + " are fun to watch.")
print("\n" + animals[1].title() + " are crazy, the best dogs, and they love to chase " + animals[0] + "!")
print("\n" + animals[2].title() + " will make you laugh.")
