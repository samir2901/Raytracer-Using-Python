class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def setPixel(self,x,y,color):
        self.pixels[y][x] = color
        
    def writeImage(self, file):

        def to_byte(c):            
            return round(max(min(c*255, 255), 0))

        file.write(f"P3 {self.width} {self.height}\n255\n") #image header
        for row in self.pixels:            
            for color in row:                  
                file.write(f"{to_byte(color.x)} {to_byte(color.y)} {to_byte(color.z)} ")
            file.write("\n")
             
