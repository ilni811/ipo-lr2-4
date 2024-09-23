import math
x = int(input("введите x: " ))
y = int(input("введите y: "))
z = int(input("введите z: "))
w = abs(math.cos(x) - math.cos(y))**(1 + 2 * math.sin(y)**2) *  (1 + z + z**2 / 2 + z**3 / 3 + z**4 / 4)
print ("ответ: ", w)