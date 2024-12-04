import re

class AOC3aSol:
    def __init__(self, p):
        self.path = p
        self.multooples = []

        with open(self.path,'r') as f:
            for line in f:
                rr = re.findall(r'mul\((\d+),(\d+)\)',line)
                if rr:
                    for rs in rr:
                        one, two = map(int, rs)
                        self.multooples.append((one,two))
                
    def getsol(self):
        accrue = 0
        for m in self.multooples:
            accrue += m[0] * m[1]
        return accrue
                
