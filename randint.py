from random import randint

gal = randint(10, 25)
mi = randint(200, 400)

def miles_per_gallon(miles, gallons):
    return miles // gallons

print("MPG equals " + str(miles_per_gallon(mi, gal)))
print("Miles equal " + str(mi))
print("Gallons equal " + str(gal))