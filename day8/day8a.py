from itertools import combinations

class AOC8aSol():
    def __init__(self,p):
        self.path = p
        self.data = []
        self.keys = set()
        self.newcoords = set()
        
        with open(self.path,'r') as f:
            for i, lines in enumerate(f.readlines()):
                self.data.append(list(lines.strip()))
            
                for l in set(self.data[i]):
                    if l != '.':
                        self.keys.add(l)
                    
        self.maxrow = len(self.data[0])
        self.maxcol = len(self.data)
    
    @staticmethod
    def searchkey(self,key):
        coords = []
        for i in range(self.maxrow):
            for j in range(self.maxcol):
                if self.data[i][j] == key:
                    coords.append((i,j))
                    
        x = list(combinations(coords,2))
        
        return 
        
    @staticmethod
    def getspots(self, x):
        
        for xs in x:
            bottom_r = 0
            bottom_l = 0
            top_r = 0
            top_l = 0
            
            rdiff,cdiff = xs[0][0] - xs[1][0] , xs[0][1] - xs[1][1]
            
            if rdiff > 0:
                bottom_r = xs[0][0] + rdiff
                top_r = xs[1][0] - rdiff
            elif rdiff == 0:
                bottom_r = xs[0][0]
                top_r = xs[0][0]
            elif rdiff < 0:
                bottom_r = xs[0][0] - rdiff
                top_r = xs[1][0] + rdiff
            if cdiff > 0:
                bottom_l = xs[0][1] + cdiff
                top_l = xs[1][1] - cdiff
            elif cdiff == 0:
                bottom_l = xs[0][1]
                top_l = xs[1][1]
            elif cdiff < 0:
                bottom_l = xs[0][1] - cdiff
                top_l = xs[1][1] + cdiff
                
            stage_new_top = (top_r,topl)
            stage_new_bot = (bottom_r,bottom_l)
            
            if stage_new_top not in self.newcoords.items():
                if 0 <= stage_new_top[0] < self.maxrows and 0 <= stage_new_top[1] < self.maxrows:
                    self.newcoords.add(stage_new_top)
            
            if stage_new_bot not in self.newcoords.items():
                if 0 <= stage_new_bot[0] < self.maxrows and 0 <= stage_new_bot[1] < self.maxcols:
                    self.newcoords.add(stage_new_bot)
        
    def solve(self):
        for s in self.keys():
            
                
