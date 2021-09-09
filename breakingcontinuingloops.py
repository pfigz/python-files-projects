#Breaking and Continuing loops

participants = ["Jen","Alex","Tina","Joe","Ben"]

position = 1
# for name in participants:
#     if name == "Tina":
#         print("About to break")
#         break
#     print("About to increment")
#     position += 1
#
# print(position)


# for currentindex in range(len(participants)):
#     print(currentindex)
#     if participants[currentindex] == "Joe":
#         print("Have breaked")
#         break
#     print("not breaked")
#
# print(currentindex+1)

for number in range(10):
    if number%3 == 0:
        print(number)
        print("Divisible by 3")
        continue
    print(number)
    print("Not divisible by 3")