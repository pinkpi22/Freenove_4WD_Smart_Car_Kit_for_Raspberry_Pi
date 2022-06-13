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
                PWM.setMotorModel(0,0,0,0)
                #FORWARD
                #-------------- SHOULD NOT DO THIS
            elif self.LMR==4:
                
                PWM.setMotorModel(2500,2500,-1500,-1500)
                #TURN RIGHT
            elif self.LMR==6:
                
                PWM.setMotorModel(4000,4000,-2000,-2000)
                #TURN RIGHT HARDER
            elif self.LMR==1:
                
                PWM.setMotorModel(-1500,-1500,2500,2500)
                #TURN LEFT
            elif self.LMR==0:
                PWM.setMotorModel(4000,4000,4000,4000)
                # Forward
            elif self.LMR==3:
               
                PWM.setMotorModel(-2000,-2000,4000,4000)
                #TURN LEFT HARDER
            elif self.LMR==7:
                #Turn Away from wall to the right slightly
                PWM.setMotorModel(1250,1250,-750,-750)
            
infrared=Boundary()
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        infrared.run()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program  will be  executed.
        PWM.setMotorModel(0,0,0,0)
