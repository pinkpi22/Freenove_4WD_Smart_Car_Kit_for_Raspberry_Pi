

from mediator import mediator
from Video import *

class colors:
    
    def run(img,xwid,ywid):
        cx = int(xwid / 2)
        cy = int(ywid / 2)
        pixel_center = img[cy, cx]
        rSum = 0
        gSum = 0
        bSum = 0
        for i in range(10):
            for j in range(10):
                rSum += img[cy-5+i][cx-5+j][0]
                gSum += img[cy-5+i][cx-5+j][1]
                bSum += img[cy-5+i][cx-5+j][2]

        b, g, r = int(rSum/100), int(gSum/100), int(bSum/100)
        colo = [r,g,b]
        print("r: " + str(r) + " | "+"g: " + str(g) + " | "+"b: " + str(b) + " | ")
        if r < 10 and g > 90:
            colo = [0,255,0]
        return colo


