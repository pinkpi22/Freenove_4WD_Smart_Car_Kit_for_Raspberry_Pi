import time
from Motor import *
import RPi.GPIO as GPIO
class Boundary:
    def __init__(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)
    def run(self):
        while True:
            self.LMR=0x00
            if GPIO.input(self.IR01)==True:
                self.LMR=(self.LMR | 4)
            if GPIO.input(self.IR02)==True:
                self.LMR=(self.LMR | 2)
            if GPIO.input(self.IR03)==True:
                self.LMR=(self.LMR | 1)
            if self.LMR==2:
                PWM.setMotorModel(-1500,-1500,2500,2500) # L: Low, M: High, R: Low
                PWM.setMotorModel(-2000,-2000,-2000,-2000)
                PWM.setMotorModel(2500,2500,-1500,-1500)
            elif self.LMR==4:
                PWM.setMotorModel(-1500,-1500,2500,2500)
                PWM.setMotorModel(-2000,-2000,-2000,-2000)
                PWM.setMotorModel(2500,2500,-1500,-1500)  # L: High, M: Low, R: Low
            elif self.LMR==6:
                PWM.setMotorModel(-2000,-2000,4000,4000)
                PWM.setMotorModel(-2000,-2000,-2000,-2000)
                PWM.setMotorModel(2000,2000,-4000,-4000) # L: High, M: High, R: Low
            elif self.LMR==1:
                PWM.setMotorModel(2500,2500,-1500,-1500)
                PWM.setMotorModel(-2000,-2000,-2000,-2000)
                PWM.setMotorModel(-1500,-1500,2500,2500) # L: Low, M: Low, R: High
            elif self.LMR==3:
                PWM.setMotorModel(4000,4000,-2000,-2000)
                PWM.setMotorModel(-2000,-2000,-2000,-2000)
                PWM.setMotorModel(-2000,-2000,4000,4000) # L: Low, M: High, R: High
            elif self.LMR==7: # All High
                #pass
                PWM.setMotorModel(-2000,-2000,-2000,-2000)
            elif self.LMR==0:
                PWM.setMotorModel(2000,2000,2000,2000)