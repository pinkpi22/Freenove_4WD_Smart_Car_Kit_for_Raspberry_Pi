

from mediator import mediator
from Video import *

class colors:
    
    def run(img,xwid,ywid):
        cx = int(xwid / 2)
        cy = int(ywid / 2)
        pixel_center = img[cy - 10, cx]
        b, g, r = int(pixel_center[0]), int(pixel_center[1]), int(pixel_center[2])
        colo = [r,g,b]
        if r < 10 and g > 130:
            colo = [0,255,0]
        return colo


