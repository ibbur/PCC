    # Aaron Frankel 2019-6-19
    # The purpose of this file is to exercise lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[1].title())

print("\n")
print(bicycles[1].title())
print(bicycles[3].title())

print("\n")
print(bicycles[-1].title() + " is the last item in the list.")

print("\n")
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print("\n")

friends = ['jonathan', 'jason', 'ron', 'mark']
flisttest_jon = "Howdy, " + friends[0].title() + "!"
flisttest_jas = "Howdy, " + friends[1].title() + "!"
flisttest_ron = "Howdy, " +friends[2].title() + "!"
flisttest_mar = "Howdy, " + friends[3].title() + "!"
print(flisttest_jon + '\n'+ flisttest_jas + '\n' + flisttest_ron + '\n' + flisttest_mar + '\n')
    # Yes, that last line was over the "80 Character limit

vehicles = ['cars','pickup trucks','motorcycles','bicycles']
cars = "I like the way Astin Martin makes " + vehicles[0] + " and would like to own one some day."
trucks = "I prefer driving " + vehicles[1] + ", most days."
motorcycles = "I miss riding " + vehicles[2] + " with my Dad."
bicycles = vehicles[-1].title() + " just don't thrill me after having ridden " + vehicles[2] + "."
print(cars + '\n' + trucks + '\n' + motorcycles + '\n' + bicycles)
