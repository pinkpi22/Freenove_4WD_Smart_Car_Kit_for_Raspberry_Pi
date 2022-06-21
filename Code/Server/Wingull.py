#                                                                       
#          @@@@.                                                               
#       @@@@@@@@@@                                                             
#         @@@@@@,%%%%                                                          
#            (#%%%%.@@@#                                                       
#               %@@@@@@@@@                                                     
#                   @@@@@@@@*                  %.%&                            
#                      .@@@@@@& @@@@@&  .*   @@@@%%%#                          
#                          ,@*.@@@@@@@@@@&&&&%*&&@@((                          
#                            @@@@@@@@@@@@@&&,                                  
#                      //*%%##,@@ @@@@@@@@,##%                                 
#                  %//,,,#%(*#,&@@@@@@@@@@@@@@@(                               
#                 ,,.,,,.                 @@@@@@@@@@@                          
#                                           .@@@@@@@@@@@@@                     
#                                              .@@@@@@@@@@@%%%%/               
#                                                 .@@@@@.%%%%%%%*@@@/          
#                                                     @%%%%%%@@@@@@@@@@@@,     
#                                                        ((@@@@@@@@@@@@@@@@@@. 
#                                                            @@@@@@@@@@        
#                                                                /@@@@@@,      
#                                                                              
import time
from Motor import *
import RPi.GPIO as GPIO
class Wingull:
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

            
            if self.LMR==0:
               #Sequence Logic
               pass
            else:
                
                PWM.setMotorModel(-600,-600,-600,-600)
                time.sleep(1)
                PWM.setMotorModel(4500,4500,-2500,-2500)
                time.sleep(0.5)
            
infrared=Wingull()
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        infrared.run()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program  will be  executed.
        PWM.setMotorModel(0,0,0,0)
