class AOC2aSol:
    def __init__(self, p):
        self.path = p
        self.sol = 0
        with open(self.path,'r') as f:
            
            csv_reader = csv.reader(f)
            for line in csv_reader:
                self.sol += self.evallist(list(map(int,line[0].split(' '))))
                
    def getsol(self):
        return self.sol
        
                
    def evallist(self,lista):
        incr = False
        decr = False
        for a in range(1, len(lista)):
            temp = lista[a] - lista[a-1]
            if abs(temp) > 3:
                return 0
            if abs(temp) == 0:
                return 0
            if temp > 0:
                if decr == False:
                    if incr == False:
                        incr = True
                else:
                    return 0
            if temp < 0:
                if incr == False:
                    if decr == False:
                        decr = True
                else:
                    return 0
                
        return 1
        
            
        
                

