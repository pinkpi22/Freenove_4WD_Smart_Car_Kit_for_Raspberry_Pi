

from mediator import mediator
from Video import *

class colors:
    
    def run(img,xwid,ywid):
        cx = int(xwid / 2)
        cy = int(ywid / 2)
        #pixel_center = img[cy, cx]
        rSum = 0 ####commented out 2
        gSum = 0
        bSum = 0
        for i in range(cy):
            for j in range(cx):
                rSum += img[cy-int(cy/2)+i][cx-int(cx/2)+j][0]
                gSum += img[cy-int(cy/2)+i][cx-int(cx/2)+j][1]
                bSum += img[cy-int(cy/2)+i][cx-int(cx/2)+j][2]

        b, g, r = int(rSum/(cy*cx)), int(gSum/(cy*cx)), int(bSum/(cy*cx))
        colo = [r,g,b]
        #print("r: " + str(r) + " | "+"g: " + str(g) + " | "+"b: " + str(b) + " | ")
        color = ["R","G","B"]
        #hue testing
        for i in range(2):
            for i in range(len(colo)-1):
                if colo[i] > colo[i+1]:
                    temp = colo[i+1]
                    colo[i+1] = colo[i]
                    colo[i] = temp
                    temp = color[i+1]
                    color[i+1] = color[i]
                    color[i] = temp
        max = colo[0]
        min = colo[2]
        R = r / 255 
        G = g / 255 
        B = b / 255 
        hue = -1
        if color[0] == "R":
            hue = (G-B)/(max-min)
        elif color[0] == "G":
            hue = 2.0 + (B-R)/(max-min)
        else: #B
            hue = 4.0 + (R-G)/(max-min)
        
        if hue < 0 and hue > -1:
            meditite.setPelipper("GREEN")
            return [0,255,0]
        elif hue < 1 and hue > 0:
            meditite.setPelipper("BLUE")
            return [0,0,255]
        elif hue < 3 and hue > 1:
            meditite.setPelipper("RED")
            return [255,0,0]
        elif hue < 4.5 and hue > 3.5:
            meditite.setPelipper("YELLOW")
            return [255,255,0]
        else:
            return [0,0,0]
        


