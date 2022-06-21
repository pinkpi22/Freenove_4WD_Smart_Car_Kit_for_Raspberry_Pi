

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
        for i in range(cy):
            for j in range(cx):
                rSum += img[cy-(cy/2)+i][cx-(cx/2)+j][0]
                gSum += img[cy-(cy/2)+i][cx-(cx/2)+j][1]
                bSum += img[cy-(cy/2)+i][cx-(cx/2)+j][2]

        b, g, r = int(rSum/400), int(gSum/400), int(bSum/400)
        colo = [r,g,b]
        print("r: " + str(r) + " | "+"g: " + str(g) + " | "+"b: " + str(b) + " | ")
        
        return colo


