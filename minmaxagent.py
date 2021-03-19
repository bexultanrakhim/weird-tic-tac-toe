import numpy as np 
from simulator import genericAgent

class minMaxAgent(genericAgent):
    def __init__(self,p):
        super().__init__(p)
    
    def moveGenerator(self,image,mp):
        # objective is to generate pos and size
        pos = np.zeros(2)
        size = 
        return pos,size