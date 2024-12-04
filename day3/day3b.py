#3b
import re

class AOC3bSol:
    def __init__(self, p):
        self.path = p
        self.multooples = []

    
        with open(self.path,'r') as f:
            do = True
            line = f.read()
        
            toks = re.split(r"\b(do|don't)\b", line)
            for t in toks:
                if do:
                    if t == 'don\'t':
                        do = False
                    else:
                        rr = re.findall(r'mul\((\d+),(\d+)\)',t)
                        if rr:
                            for rs in rr:
                                one, two = map(int, rs)
                                self.multooples.append((one,two))
                elif not do:
                    if t == 'do':
                        do = True
                
        
    def getsol(self):
        accrue = 0
        for m in self.multooples:
            accrue += m[0] * m[1]
        
        return accrue
                
