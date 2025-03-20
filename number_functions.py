import math
x = 4567896
print(math.sqrt(x))
print(math.pi)
print(math.floor(56.88))
print(math.ceil(56.88))

radius=54
height=145

volume=22/7 *radius*radius*height
volume=round(volume,1)
print(volume)

sa= 2*22/7*radius*(radius+height)
sa=round(sa,1)
print(sa)

result = 10 + 20 / 5 * 6 - 3 * (5+2)
print(result)

my_list=[0,1,2,3,4,5,6,7,8,9]
#        0,1,2,3,4,5,6,7,8,9
#      -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:step]

print(my_list[2:-1:2])


