#Classes Pets: Part A, B, C, D... This doesn't make a lot of sense to me. This kid sucks at teaching.

class Pet:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p
    #getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    #setters
    def setName(self, xname):
        self.name = xname

    def setAge(self, xage):
        self.age = xage

    def setHunger(self, xhunger):
        self.hunger = xhunger

    def setPlayful(self, xplayful):
        self.playful = xplayful

    def __str__(self):
        return (self.name + "is " + str(self.age) + " years old.")

class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, FavoriteToy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.FavoriteToy = FavoriteToy

    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with " + self.FavoriteToy)
        else:
            return ("Dog doesn't want to play")

class Cat(Pet):
    def __init__(self, name, age, hunger, playful, place):
        Pet.__init__(self, name, age, hunger, playful)
        self.favoritePlaceToSit = place

    def wantsToSit(self):
        if self.playful == False:
            print("Cat wants to sit on the " + self.favoritePlaceToSit)
        else:
            print("The cat wants to play")

    def __str__(self):
        return (self.name + " likes to sit on the " + self.favoritePlaceToSit)

class Human:
    def __init__(self, name, Pets):
        self.name = name
        self.Pets = Pets

    def hasPets(self):
        if len(self.Pets) != 0:
            return "yes"
        else:
            return "no"


huskyDog = Dog("Snowball", 5, False, True, "Husky", "Stick")
Play = huskyDog.wantsToPlay()
print(Play)

huskyDog.playful = False

Play = huskyDog.wantsToPlay()
print(Play)

typicalCat = Cat("Whiskers", 3, False, False, "sofa")
typicalCat.wantsToSit()
print(typicalCat)
print(huskyDog)


yourAverageHuman = Human("Alice", [huskyDog, typicalCat])

hasPet = yourAverageHuman.hasPets()

print(hasPet)
print(yourAverageHuman.Pets[1].name)