def relation_to_luke(name):

    family = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in-law",
        "R2D2": "droid"
        }

    return "Luke, I am your " + family[name] + "."

print(relation_to_luke("R2D2"))
