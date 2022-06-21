from Main import *
from Video import *
import cv2

class ballColor:
    def colorDisplay():
        cap = cv2.VideoCapture(2)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        frame = cap.read()
        height, width = frame.shape

        hsvframe = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cx = int(width/2)
        cy = int(height/2)

        pixel_center = hsvframe[cy, cx]
        hue_value = pixel_center[0]

        # if hue_value < 22 or hue_value > 170:
        #     ledDisplay.ledIndex(0x01,255,0,0)
        # elif hue_value < 33:
        #     ledDisplay.ledIndex(0x40,255,255,0)
        # elif hue_value < 78:
        #     ledDisplay.ledIndex(0x80,0,255,0)
        # elif hue_value < 131:
        #     ledDisplay.ledIndex(0x10,0,255,255)

        pixel_center_bgr = frame[cy, cx]
        b= int(pixel_center_bgr[0])
        g= int(pixel_center_bgr[1])
        r = int(pixel_center_bgr[2])
