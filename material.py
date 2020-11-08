from color import Color 

class Material:
    def __init__(self, baseColor : Color = Color(1,1,1), ambient : float = 0.5, diffuse : int = 1, specular : int = 1):
        self.baseColor = baseColor
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
    
    def colorAt(self, position):
        return self.baseColor