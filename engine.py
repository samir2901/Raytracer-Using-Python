from scene import Scene
from image import Image
from ray import Ray 
from point import Point
from color import Color

class RenderEngine:
    """Renders into 2D image from 3D"""
    def render(self,scene:Scene):
        width = scene.width
        height = scene.height
        aspectRatio = width / height
        x0 = -1.0
        x1 = 1.0
        dx = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspectRatio
        y1 = 1.0 / aspectRatio
        dy = (y1 - y0) / (height - 1)

        camera = scene.camera
        img = Image(width, height)
        for j in range(height):
            y = y0 + j * dy 
            for i in range(width):
                x = x0 + i * dx 
                ray = Ray(camera, Point(x,y) - camera)
                img.setPixel(i, j, self.rayTrace(ray, scene))
            print(f"{int(float(j)/float(height) * 100)}%", end="\r")

        return img 
    
    def rayTrace(self, ray:Ray, scene:Scene):
        color = Color()
        distHit, objHit = self.findNearest(ray, scene)
        if(objHit is None):
            return color 
        hitPos = ray.origin + ray.direction * distHit
        hitNormal = objHit.normal(hitPos)
        color += self.colorAt(objHit, hitPos, hitNormal,scene)   
        return color   

    def findNearest(self, ray : Ray, scene : Scene):
        distMin = None 
        objHit = None 
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if(dist is not None) and (objHit is None or dist < distMin):
                distMin = dist
                objHit = obj
        return (distMin, objHit)
    
    def colorAt(self, objHit, hitPos, normal, scene : Scene):
        mat = objHit.material
        objColor = mat.colorAt(hitPos)
        toCam = scene.camera - hitPos
        specularK = 100
        color = mat.ambient * Color(0,0,0)
        for light in scene.lights:
            toLight = Ray(hitPos,light.position - hitPos)
            #diffuse shading 
            color += objColor * mat.diffuse * max(normal.dot(toLight.direction), 0)

            #specular shading
            halfVector = (toLight.direction + toCam).normalized()
            color += light.color * mat.specular * max(normal.dot(halfVector), 0) ** specularK
        return color 
        
                                

        
    