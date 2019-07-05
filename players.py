# Aaron Frankel 2019-7-5
# The purpose of this file is to learn slices

print("\n")

players = ['charles', 'martina', 'michael','florence','eli']
print(players[0:3])

print("\n")

print(players[1:4])

print("\n")

print(players[:4])

print("\n")

print(players[2:])

print("\n")

print(players[-3:])

print("\n")

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\n")
