#Homework #4: Lists

myUniqueList = []               #List variable
myLeftovers = []                #Left over list variable

def add(a):                     #Unique list function with extra credit else statement
    if a not in myUniqueList:
        myUniqueList.append(a)
        print(True)
    else:
        myLeftovers.append(a)
        print(False)


add("Two")
add(2)
add(2)
add("Two")
add("Hello World")
add(True)
print(myUniqueList)
print(myLeftovers)


