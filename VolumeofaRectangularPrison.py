l = int(input("Length"))
w = int(input("Width"))
h = int(input("Height"))


def volume(p1, p2, p3):
    return p1 * p2 - p3


print("The volume of the rectangular prism is " + str(volume(l, w, h)) + " cubic feet")

