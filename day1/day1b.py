import csv
import re

class AOC1bSol:
    def __init__(self, p):
        self.path = p
        self.left = set()
        self.right = []
    
        with open(self.path,'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                rr = re.findall(r'(\d{5})',line[0])
                if rr:
                    self.left.add(int(rr[0]))
                    self.right.append(int(rr[1]))
        
    def getsol(self):
        self.dict1 = {}
        accrue = 0
        
        for l in self.left:
            for r in range(len(self.right)):
                if l == self.right[r]:
                    if self.dict1.get(l,0) == 0:
                        self.dict1[l] = l
                    else:
                        self.dict1[l] += l
                        
        for _,v in self.dict1.items():
            accrue += v 
        
        return accrue
                
