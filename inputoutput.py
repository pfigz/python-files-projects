#Input & Output

#var = input("Message to the user")

# name = input("Enter your name: ")
# print(name)

# age = input("Enter your age: ")
# print(age)

scores = []

for i in range(5):
    currentScore = float(input("Please enter the score "+str(i+1)+": \n"))
    scores.append(currentScore)
    print("The score you entered was:\n",currentScore,"nice")

print(scores)