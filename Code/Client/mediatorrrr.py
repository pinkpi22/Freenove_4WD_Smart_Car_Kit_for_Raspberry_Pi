import colorsys
import numpy as np
import cv2
import socket
import os
import io
import time
import imghdr
import sys
import math
from threading import Timer
from threading import Thread
from PIL import Image
from Command import COMMAND as cmd
from Thread import *
from Client_Ui import Ui_Client
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class mediator:
    red = 0
    green = 0
    blue = 0
    button = ""
    def __init__(self):
        self.endChar='\n'
        self.intervalChar='#'

    def colorchoose(self, img, xmin, xmax, ymin, ymax):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cx = int((xmin+xmax) / 2)
        cy = int((ymin+ymax) / 2)
        pixel_center = hsv[cy, cx]
        hue_value = pixel_center[0]
        sat_value = pixel_center[1]
        val_value = pixel_center[2]
        (h, s, v) = (hue_value/179, sat_value/255, val_value/255)
        (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
        self.red = int(r*255)
        self.green = int(g*255)
        self.blue = int(b*255)
        self.color=self.intervalChar+str(self.red)+self.intervalChar+str(self.green)+self.intervalChar+str(self.blue)+self.endChar
