

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
        for i in range(100):
            for j in range(100):
                rSum += img[cy-50+i][cx-5+j][0]
                gSum += img[cy-50+i][cx-5+j][1]
                bSum += img[cy-50+i][cx-5+j][2]

        b, g, r = int(rSum/100), int(gSum/100), int(bSum/100)
        colo = [r,g,b]
        print("r: " + str(r) + " | "+"g: " + str(g) + " | "+"b: " + str(b) + " | ")
        if b < 150 and g < 150 and r < 10:
            colo = 
        return colo


