def volume(radius, height):
    v = 3.14 * radius * radius * height
    return v

def area(radius, height):
    a = ((2 * 3.14 * radius) * height) + ((3.14 * radius ** 2) * 2)
    return a
r=3
h=4
print("The volume of the cylinder is: ",volume(r, h))
print("The surface area of the cylinder is: ",area(r, h))
