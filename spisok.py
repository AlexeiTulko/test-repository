listing = [] #two biggest numbers
for i in range(int(input('Listing = '))):
    listing.append(int(input('{}number = '.format(i+1))))
two_biggest = sorted(listing, reverse=True)[0:2]
print(listing)
print(two_biggest)
