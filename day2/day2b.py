class AOC2bSol:
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
        faults = 0
        incr = False
        decr = False
        problem = set()
        for a in range(1, len(lista)):
            temp = lista[a] - lista[a-1]
            
            if abs(temp) > 3 or temp == 0:
                faults += 1
                problem.add(a)
                problem.add(a-1)
            
            if temp > 0:  
                if decr:  
                    faults += 1
                    problem.add(a)
                    problem.add(a-1)
                    
                incr = True
                decr = False
            elif temp < 0:  
                if incr:  
                    faults += 1
                    problem.add(a)
                    problem.add(a-1)
                decr = True
                incr = False

            if faults >= 1:
                for idx in sorted(problem, reverse=True):
                    new_list = lista[:idx] + lista[idx + 1:]
                    if self.evallistpass(new_list) == 1:
                        return 1
                return 0
        
         
        return 1
    
    def evallistpass(self,listb):
        incr = False
        decr = False
        for a in range(1, len(listb)):
            temp = listb[a] - listb[a-1]
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
        
