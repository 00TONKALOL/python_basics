def volume_cylinder(radius , height):
    """Calculate the volume of a cylinder in centimeters."""
    v = 22/7 * radius**2 * height
    return v
print(volume_cylinder(9,10))
print(round(volume_cylinder(9.73,10.93), 2))
v1=volume_cylinder(height= 17 , radius= 15)
print(v1)

def volume_cone(radius , height ,decimals=2):
    v = 1/3 *22/7 * radius**2 * height
    v = round(v, decimals)
    return v
print(volume_cone(23,16)  )
print(round(volume_cone(29,16),2))
