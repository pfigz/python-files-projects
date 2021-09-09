#Homework #9: Classes

import random

class Vehicle:

    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False


class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0, isDriving=False):
        Vehicle.__init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance)
        self.isdriving = isDriving

    def drive(self):
        self.isdriving = True

    def stop(self):
        if self.isdriving:
            self.isdriving = False
            self.TripsSinceMaintenance += 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True
#Added this automatic maintenance function, but commented out as it was not required
            # if self.NeedsMaintenance == True:
            #      Vehicle.repair(self)
            #      print("Your vehicle has been repaired")

def drive(car):
    driveTime = random.randint(1,150)
    for i in range(driveTime):
        car.drive()
        car.stop()


Car1 = Cars("Nissan", "Sentra", 2000, 3000)
Car2 = Cars("Honda", "Accord", 2001, 2900)
Car3 = Cars("Ford", "Ranger", 2002, 3500)


while True:
    drive(Car1)
    drive(Car2)
    drive(Car3)

    print("Make: " + Car1.Make + "," + Car2.Make + "," + Car3.Make)
    print("Model: " + Car1.Model + "," + Car2.Model + "," + Car3.Model)
    print("Year: " + str(Car1.Year) + "," + str(Car2.Year) + "," + str(Car3.Year))
    print("Weight: " + str(Car1.Weight) + "," + str(Car2.Weight) + "," + str(Car3.Weight))
    print("Needs Maintenance: " + str(Car1.NeedsMaintenance) + "," + str(Car2.NeedsMaintenance) + "," + str(Car3.NeedsMaintenance))
    print("Trips since Maintanence: " + str(Car1.TripsSinceMaintenance) + "," + str(Car2.TripsSinceMaintenance) + "," + str(Car3.TripsSinceMaintenance))


    break




