
import os

fileName = input("What do you want the filename to be?") + ".txt"


if os.path.isfile(fileName):
    choice = input("Do you want to: \n A) Read the File \n B) Delete the file and start over \n C) Append the file \n ")

    if choice == "A":
        File = open(fileName, 'r')
        lines = File.readlines()
        print(lines)
        File.close()

    elif choice == "B":
        os.remove(fileName)
        File = open(fileName,"w")
        File.close()


    elif choice == "C":
        File = open(fileName,"w")
        Files = [File]
        fileAppend = input("What would you like to append to the file?")
        Files.append(fileAppend)
        File.write(str(Files))

else:
    data = input("Please enter a note.")
    File = open(fileName, "w")
    File.write(data)
    File.close()
    print("Your file has been created!")

File.close()

