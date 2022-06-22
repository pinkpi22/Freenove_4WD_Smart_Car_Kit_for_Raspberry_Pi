from Client_Ui import *
from Command import COMMAND as cmd                                                                                

class mediator:
    label = ""
    colo = [255,0,0]
    type = ""

    def setColo(self,input):
        self.colo = input

    def getColo(self):
        return self.colo

    def setLabel(self,input):
        self.label = input

    def getLabel(self):

        return self.label

    def setType(self,input):
        self.type = input

    
    