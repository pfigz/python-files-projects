celsius = float(input("Degrees Celsius"))

def fahrenheit(c):
    return round((1.8 * c + 32), 1)

print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)))

