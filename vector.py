from math import * 

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z 

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        assert not isinstance(scalar, Vector)
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
   
    def __truediv__(self, scalar):
        assert not isinstance(scalar, Vector)
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
        
    def magnitude(self):
        mag = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return mag 

    def normalized(self):
        mag = self.magnitude()
        self.x/=mag
        self.y/=mag
        self.z/=mag
        return self 
    

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
        

        

#testing
'''
v1 = Vector(1,2,2)
v2 = Vector(3,3,3)
print(v1)
print(v1 - v2)
print(v1/4)
print(v1.magnitude())
print(v1.normalized())
'''




    

