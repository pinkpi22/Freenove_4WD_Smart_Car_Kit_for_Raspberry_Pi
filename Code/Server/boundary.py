import time
from Motor import *
import RPi.GPIO as GPIO
class boundary:
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
            PWM.setMotorModel(1000, 1000, 1000, 1000)
            if GPIO.input(self.IR01)==True:# left sensor
                self.LMR=(self.LMR | 4)
            if GPIO.input(self.IR02)==True: #middle senor
                self.LMR=(self.LMR | 2)
            if GPIO.input(self.IR03)==True: #right sensor
                self.LMR=(self.LMR | 1)  
            
            if self.LMR > 0 and self.LMR <4:
                #pass
                PWM.setMotorModel(-1000,-1000,-1000,-1000)
                time.sleep(3.0)
                PWM.setMotorModel(-2000, -2000, 1000, 1000)
                time.sleep(0.8)
            
            elif self.LMR > 4 and self.LMR < 8:
                #pass
                PWM.setMotorModel(-1000,-1000,-1000,-1000)
                time.sleep(3.0)
                PWM.setMotorModel(1000, 1000, -2000, -2000)
                time.sleep(0.8)

            # if self.LMR==2:     #luw #llw #ruw #rlw  
            #     PWM.setMotorModel(0,0,0,0) 
            # elif self.LMR==4:
            #     PWM.setMotorModel(2500,2500,-1500,-1500)
            # elif self.LMR==6:
            #     PWM.setMotorModel(4000,4000,-2000,-2000)
            # elif self.LMR==1:
            #     PWM.setMotorModel(-1500,-1500,2500,2500)
            # elif self.LMR==3:
            #     PWM.setMotorModel(2000,2000,-4000,-4000)


box=boundary()
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        box.run()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program  will be  executed.
        PWM.setMotorModel(0,0,0,0)
