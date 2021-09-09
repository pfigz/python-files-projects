# Class Inheritance

# class ClassName:
#
#     def __init__(self):
#         self.Attribute
#
#     def AnotherFunction(self):
#         Action(s)

class Team:
    def __init__(self, Name = "Name", Origin = "Origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin

    def DefineTeamName(self, Name):
        self.TeamName = Name

    def DefineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin

# class InheritanceClassName(ParentClass):
#     def __init__(self, Input1, Input2):
#         ParentClass.__init__(self)
#         self.Attribute1 = Input1
#         self.Attribute2 = Input2
#         self.Attribute3 = 0
#
#     def AnotherMethod(self):
#         Action(s)

class Player(Team):
    def __init__(self, PName, PPoints, TeamName, TeamOrigin):
        Team.__init__(self, TeamName, TeamOrigin)
        self.PlayerName = PName
        self.PlayerPoints = PPoints

    def ScoredPoint(self):
        self.PlayerPoints += 1

    def setName(self, Name):
        self.PlayerName = Name

    def __str__(self):
        return self.PlayerName + " has scored: " + str(self.PlayerPoints) + " points."

Player1 = Player("Sid", 0, "Sharks", "Chicago")

print(Player1.PlayerName, Player1.PlayerPoints)
#Player1.DefineTeamName("Sharks")
print(Player1.TeamName)
print(Player1.TeamOrigin)

Player1.ScoredPoint()
print(Player1.PlayerPoints)

Player1.setName("Lee")

print(Player1.PlayerName)

print(Player1)


