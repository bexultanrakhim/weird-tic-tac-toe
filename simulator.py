import numpy as np

class World:
    def __init__(self,):
        self.mp = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(state())
            self.mp.append(row)
        self.players = []

    def setAgent(self,agent):
        self.players.append(agent)
    def getMap(self,):
        return self.mp
    def createMapImage(self,player):
        map_image = np.zeros((3,3))
        for i in range(3):
            for j in range(3):
                p = self.mp[i][j].getP()
                if(p == "X"):
                    map_image[i,j] = 2*(player-1.5)*self.mp[i][j].getSize()
                elif p == "O" :
                    map_image[i,j] = -2*(player-1.5)*self.mp[i][j].getSize()
        return map_image
    def checkWin(self):
        for i in range(3):
            #check rows
            r0 = self.mp[i][0].getP()
            r1 = self.mp[i][1].getP()
            r2 = self.mp[i][2].getP()
            if(r0 != "_" and r0 == r1 and r0 == r2):
                return True, r0
            
            c0 = self.mp[0][i].getP()
            c1 = self.mp[1][i].getP()
            c2 = self.mp[2][i].getP()
            
            if(c0 != "_" and c0 == c1 and c0 == c2):
                return True, c0 
        
        d0 = self.mp[0][0].getP()
        d1 = self.mp[1][1].getP()
        d2 = self.mp[2][2].getP()    
        if(d0 != "_" and d0 == d1 and d0 == d2):
            return True, d0
        
        rd0 = self.mp[0][2].getP()
        rd1 = self.mp[1][1].getP()
        rd2 = self.mp[2][0].getP()    
        if(rd0 != "_" and rd0 == rd1 and rd0 == rd2):
            return True, rd0
        return False , "_"
    
    def gameFinished(self):
        s1, a = self.players[0].checkWin(self.createMapImage(1))
        s2, b = self.players[1].checkWin(self.createMapImage(2))
        if(s1 or s2):
            if(a > b):
                print("Winner: "+"X")
            else:
                print("Winner: "+"O")
            
            return True

        if(self.players[0].leftMoves()<=0 and self.players[1].leftMoves()<=0):
            print("no moves left: draw")
            return True
        return False

    def step(self,):
        #move agent1
        self.mp = self.players[0].tryMove(self.mp,self.createMapImage(1))

        if(self.gameFinished()):
            self.players[0].inform_result(self.createMapImage(1))
            self.players[1].inform_result(self.createMapImage(2))
            return False
        else:
            self.players[1].inform_result(self.createMapImage(2))
        #move agent2
        self.mp = self.players[1].tryMove(self.mp,self.createMapImage(2))
        #check if finished
        if(self.gameFinished()):
            s, _  = self.players[1].checkWin(self.createMapImage(2))
            if( s > 0): 
                self.players[0].inform_result(self.createMapImage(1))
                self.players[1].inform_result(self.createMapImage(2))
            else:
                self.players[0].inform_result(self.createMapImage(1))
                self.players[1].inform_result(self.createMapImage(2))
            return False
        else:
            self.players[0].inform_result(self.createMapImage(1))
        return True
              
class state:
    def __init__(self,p="_",size=0):
        self.p = p
        self.size = size
    def getSize(self):
        return self.size
    def getP(self):
        return self.p
    
    def __repr__(self):
        return self.p + str(self.size)
    def __str__(self):
        return self.p + str(self.size)

class genericAgent:
    def __init__(self,p):
        self.size_list = [5,4,3,2,1]
        self.p = p
        self.history = []
        self._buffer ={}
    
    def getHistory(self):
        return self.history

    def checkWin(self,image):
        for i in range(3):
            #check rows
            r0 = image[i][0]
            r1 = image[i][1]
            r2 = image[i][2]
            if(r0 != 0 and r1 != 0 and r2 != 0 and np.sign(r0) == np.sign(r1) and np.sign(r0) == np.sign(r2)):
                return True, -np.sign(r0)
            
            c0 = image[0][i]
            c1 = image[1][i]
            c2 = image[2][i]
            
            if(c0 != 0 and c1 != 0 and c2 != 0 and np.sign(c0) == np.sign(c1) and np.sign(c0) == np.sign(c2)):
                return True, -np.sign(c0)
             
        
        d0 = image[0][0]
        d1 = image[1][1]
        d2 = image[2][2]
        if(d0 != 0 and d1 != 0 and d2 != 0 and np.sign(d0) == np.sign(d1) and np.sign(d0) == np.sign(d2)):
            return True, -np.sign(d0)
            
        rd0 = image[0][2]
        rd1 = image[1][1]
        rd2 = image[2][0]    
        
        if(d0 != 0 and d1 != 0 and d2 != 0 and np.sign(d0) == np.sign(d1) and np.sign(d0) == np.sign(d2)):
            return True, -np.sign(d0)
        
        return False , 0
    
    def checkValid(self,mp,pos,size):
        if(mp[pos[0]][pos[1]].getSize()<size and mp[pos[0]][pos[1]].getP() != self.p):
            return True
        else: 
            return False
    def leftMoves(self,):
        return len(self.size_list)
    
    def createState(self,size):
            return state(p=self.p,size=size)

    def moveGenerator(self,image,mp):
        #random move
        pos = np.random.randint(0,3,size=2)
        size_indx = np.random.randint(0,len(self.size_list))
        size = self.size_list[size_indx]
        return pos,size
    
    def inform_result(self,image):
        s, reward = self.checkWin(image)
        if(self._buffer):
            this = {}
            this["state"] = self._buffer["state"]
            this["action"] = self._buffer["action"]
            this["next_state"] = image
            this["reward"] = reward
            self.history.append(this)
            self._buffer = {}
    def tryMove(self,mp,image):
        while True:
            pos,size = self.moveGenerator(image,mp)
            if(not (size in self.size_list)):
                print(self.p + ": not legal move, try again")
                continue
            if(self.checkValid(mp,pos,size)):
                self._buffer["state"] = image
                self._buffer["action"] = [pos,size]
                self.size_list.remove(size)
                st = self.createState(size)
                mp[pos[0]][pos[1]] = st
                break
            else:
                print(self.p+": invalid play, try again")
        return mp

class humanAgent(genericAgent):
    def __init__(self,p):
        super().__init__(p)

    def moveGenerator(self,image,mp):
        for i in mp:
            print(i)
        print(" ")
        
        inpt = input()
        lst = inpt.split(" ",3)
        pos = np.array([int(lst[0]),int(lst[1])])
        size = int(lst[2])
        return pos,size