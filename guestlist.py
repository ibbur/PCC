guestlist =['Dad', 'Pappaw', 'Ben Franklin']
print(guestlist)

print("\n" + guestlist[0] + ", I'd like to invite you to dinner. There will be interesting guests.")
print("\n" + guestlist[1] + ", please join me for a small dinner party.")
print("\n" + guestlist[2] + ", please join us for a dinner party. You'll find the guests interesting and conversations enlightening.")

print('\n --- Change the guest list. --- ')
print('\n' + guestlist[2] + ' cannot make it to the dinner. We will invite the person we should have included to begin with.')
guestlist[2] = "Shaush"
print("\n" + guestlist[2] +", please join us for dinner. We'd love to see you, and I owe you an appology or twelve.")

print('\nWe found a larger venue. Now we can add three more guests.')
guestlist.insert(3, 'Morty')
guestlist.insert(4, 'Gemmaw')
guestlist.append('Joe')
print("\nLet's see who the new additions are.")
print(guestlist)
print(guestlist[5] + ", join us for dinner. It would be great to see you again.")
print(guestlist[3] + ", I'd love to meet you. Please join us for dinner.")
print(guestlist[4] + ", won't you join us for dinner. I'd love to see you--so much to catch up on.")

print('\nThere is a seating issue, folks. Removing guests, unfortunately.')
guestlist_pop = guestlist.pop()
print("\nI'm terriblely sorry, " + guestlist_pop + ". There's been a reduction in available seating. We'll arrange anther dinner in short order, so we can all get to gether.")
guestlist_pop = guestlist.pop()
print("\nI'm very sorry, " +  guestlist_pop + ". The jerk who wrote the exercise removed seats from our dinner. We'll arrange another dinner soon.")
guestlist_pop = guestlist.pop()
print("\nMy deepest appologies, " + guestlist_pop + ". The wanker who wrote the great python book removed seats from our party. We'll arrange another soon.")
guestlist_pop = guestlist.pop()
print("\nNow I owe you a thirteenth appology, " + guestlist_pop + ". The Nerf herder who wrote the book cut our seating. We'll set a date for dinner, just you and I. And we'll arrange another dinner party.")

print("\nOur guest list now consists of " + guestlist[0] + " and " + guestlist[1] + ".")
print("\n" + guestlist[0] + " and " + guestlist[1] + ", there are still seats for the two of you. Please be sure to join me for dinner.")

print("\nWell shit! Now the author is canceling the whole party.")
print(guestlist)
del guestlist[1]
print(guestlist)
del guestlist[0]
print(guestlist)
