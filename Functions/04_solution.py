import math

def circular_stats(radius):
  area =  math.pi * radius ** radius
  circumference = 2 * math.pi * radius 

  return area,circumference

a,c = circular_stats(3);
print("area ",a,"circuferr ", c);

