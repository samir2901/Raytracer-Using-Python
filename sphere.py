from math import sqrt
from point import Point
from ray import Ray
from material import Material

class Sphere:    
    def __init__(self, center : Point, radius : float, material : Material):
        self.center = center
        self.radius = radius
        self.material = material
    
    def intersects(self, ray:Ray):
        '''
        Checks if ray intersects with sphere. Returns distance if intersects
        '''            
        sphereToRay = ray.origin - self.center
        b = 2 * ray.direction.dot(sphereToRay)
        c = sphereToRay.dot(sphereToRay) - self.radius * self.radius
        discriminant = b * b - 4 * c
        if(discriminant >=0):
            dist = (- b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist 
        return None 

    def normal(self, surfacePoint : Point):
        return (surfacePoint - self.center).normalized()
