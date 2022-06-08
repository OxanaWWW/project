import math
print("переход к полярным координатам")
def pol2cart(r, phi):
    x = r * math.cos(math.radians(phi))
    y = r * math.sin(math.radians(phi))
    return(x, y)

r=float(input("введите радиус:"))
phi=float(input("введите угол поворота:"))

print("координата  r = ", r, "и phi = ", phi, "координаты  = ", pol2cart(r, phi))
