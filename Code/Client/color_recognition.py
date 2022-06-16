

from mediator import mediator
from Video import *

class colors:
    
    def run(img,xwid,ywid):
        cx = int(xwid / 2)
        cy = int(ywid / 2)
        pixel_center = img[cy, cx]
        b, g, r = int(pixel_center[0]), int(pixel_center[1]), int(pixel_center[2])
        colo = [r,g,b]
        print("R: " + str(r) + "G: " + str(g) + "B: " + str(b))
        return colo


