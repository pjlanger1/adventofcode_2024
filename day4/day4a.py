class AOC4aSol:
    def __init__(self, p):
        self.path = p
        self.countxmas = 0
        self.dest = []
    
        with open(self.path,'r') as f:
            for l in f.readlines():
                self.dest.append(l.strip('\n'))
    
        self.maxi = len(self.dest[0])
        self.maxj = len(self.dest)
        
        
     

    def check_position(self, i, j):
        directions = {
            "horizontal": [(0, -1), (0, 1)],
            "vertical": [(-1, 0), (1, 0)],
            "right_diagonal": [(-1, 1), (1, -1)],
            "left_diagonal": [(-1, -1), (1, 1)]
        }

        ret = {k: [(i, j)] for k in directions}  

        for n in range(1, 5):  
            for k, v in directions.items():
                for r, c in v:
                    ni, nj = i + r * n, j + c * n
                    if 0 <= ni < self.maxi and 0 <= nj < self.maxj:
                        ret[k].append((ni, nj))

        self.makestring(self.valid_path(ret))
        
        return None

    
    def valid_path(self,arcs):
        sorte = {}
    
        for g, p in arcs.items():
            sorte[g] = sorted(p, key=lambda x: (x[0], x[1]))
            
        return sorte
    
    def makestring(self,sortedarcs):
        for k,v in sortedarcs.items():
            temp = ''.join(self.dest[vs[0]][vs[1]] for vs in v)
            if 'XMAS' in temp:
                self.countxmas += 1
            if 'SAMX' in temp:
                self.countxmas += 1
        return None
            
            

    
    def getsol(self):
        for r in range(0,self.maxi):
            for c in range(0,self.maxj):
                self.check_position(r,c)
        
        return self.countxmas
                
                
    
        
    
