from point import Point
from color import Color

class Light:
    def __init__(self, position : Point, color : Color = Color(1,1,1)):
        self.position = position
        self.color = color
        
