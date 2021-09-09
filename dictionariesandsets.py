#Homework #7: Dictionaries and Sets


song_info = {"Song": "Liars and Thieves",
             "Artist": "Brodero",
             "Genre": "Rock",
             "Duration": "197",
             "Year Released": "2017",
             "Written by": "Brodero",
             "Produced by": "Brodero",
             "Recorded at": "Green Chapel Studios"
             }

for key in song_info:
    print(key,":", song_info[key])

#Extra Credit
# key = str(input("Name an attribute or credential of my favorite song\n"))
# value = str(input("Guess a value for this credential or attribute\n"))
#
# def guess():
#     if key and value in song_info[key]:
#         return True
#     else:
#         return False
#
# print(guess())



