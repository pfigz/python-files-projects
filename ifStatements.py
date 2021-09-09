def function(a, b, c):
    output = False
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        if a == b or b == c or c == a:
            output = True
    except ValueError:
        print("ValueError: must be an integer")
    finally:
        print(a, b, c)
        return output


print(function(1, "a", 3))
print(function(1, 1, 2))
