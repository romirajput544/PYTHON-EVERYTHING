import math

def cirlce_stats(radius):
    area = math.pi*radius**2
    circum = 2*math.pi*radius
    return area,circum


a,c=cirlce_stats(3)
print("Area : ",a,"Circumference: ",c)