from image import Image
from color import Color
from vector import Vector
from point import Point 
from sphere import Sphere
from scene import Scene 
from engine import RenderEngine
from light import Light
from material import Material

def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    mat = Material(Color(1,0,0))
    objects = [Sphere(Point(0,0,0), 0.5, mat)]
    lights = [Light(Point(1.5,-0.5,-10), Color(1,1,1))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    img = engine.render(scene)    
    
    f = open("test.ppm","w")
    img.writeImage(f)
    f.close()
    
if __name__ == "__main__":
    main()

