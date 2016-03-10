import maya.cmds as cmds 

class LocatorSetup(object):
    """
    This class will create locators for joint placement
    part needs to be
    {'name' : ['translate', 'scale', 'lock attr info']}
    """
    
    def __init__(self):
        self.adjustCtrls = []
        
    def createLocator(self, part):
        self.placeLocs = part
        
        for oneLoc in self.placeLocs.keys():
            cmds.spaceLocator( n = oneLoc) #Joint control
            cmds.move(self.placeLocs[oneLoc][0][0], self.placeLocs[oneLoc][0][1], self.placeLocs[oneLoc][0][2], r = True)
            cmds.scale(self.placeLocs[oneLoc][1], self.placeLocs[oneLoc][1], self.placeLocs[oneLoc][1]) 
            if self.placeLocs[oneLoc][2]: 
                cmds.setAttr(oneLoc + '.' + self.placeLocs[oneLoc][2] , lock = True)#CTRL Move
            
            self.adjustCtrls.append(oneLoc)
        
        return self.placeLocs.keys()
        
    
    """
    def saveLocatorPos(self):
    
    def loadLocatorPos(self):
    """