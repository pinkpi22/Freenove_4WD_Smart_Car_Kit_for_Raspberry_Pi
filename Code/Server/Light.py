import time
from Motor import *
from ADC import *
class Light:
    def run(self):
        try:
            self.adc=Adc()
            self.PWM=Motor()
            self.PWM.setMotorModel(0,0,0,0)
            while True:
                L = self.adc.recvADC(0)
                R = self.adc.recvADC(1)
                if abs(L-R)<0.15:
                    self.PWM.setMotorModel(0,0,0,0)
                elif L < 2.75 and R < 2.75 :
                    self.PWM.setMotorModel(100,100,100,100) 
                elif L > 2.76 or R > 2.76:
                    if L > R :
                        self.PWM.setMotorModel(-1200,-1200,1400,1400)
                        
                    elif R > L :
                        self.PWM.setMotorModel(1400,1400,-1200,-1200)
                    
        except KeyboardInterrupt:
           led_Car.PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    print ('Program is starting ... ')
    led_Car=Light()
    led_Car.run()


        
    

