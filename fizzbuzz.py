
for number in range(1, 101):
    print(number)
    if (number%15 == 0):
        print("Fizzbuzz")
    elif (number %3 == 0):
        print("Fizz")
    elif (number%5 == 0):
        print("Buzz")
    else:
        if (number%2 == 1):
            print("Prime")