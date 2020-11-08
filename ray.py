from vector import Vector
from point import Point
class Ray:
    def __init__(self, origin : Point, direction : Vector):
        self.origin = origin
        self.direction = direction.normalized()

        