

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
        for i in range(20):
            for j in range(20):
                rSum += img[cy-10+i][cx-10+j][0]
                gSum += img[cy-10+i][cx-10+j][1]
                bSum += img[cy-10+i][cx-10+j][2]

        b, g, r = int(rSum/400), int(gSum/400), int(bSum/400)
        colo = [r,g,b]
        print("r: " + str(r) + " | "+"g: " + str(g) + " | "+"b: " + str(b) + " | ")
        
        return colo


