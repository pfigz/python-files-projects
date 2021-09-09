#Participant Data, Part A

participant_number = 2
participant_data = []
output_file = open("ParticipantData.txt", "w")

registered_participants = 0
while registered_participants < participant_number:
    temp_part_data = [] #name,country of origin, age
    name = input("Please enter your name: ")
    temp_part_data.append(name)
    country = input("Please enter your country of origin: ")
    temp_part_data.append(country)
    age = int(input("Please enter your age: "))
    temp_part_data.append(age)
    print(temp_part_data)
    participant_data.append(temp_part_data)
    print(participant_data)
    registered_participants += 1

for participant in participant_data:
    for data in participant:
        output_file.write(str(data))
        output_file.write(" ")
    output_file.write("\n")

output_file.close()


