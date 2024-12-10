from itertools import product
import re

class AOC7aSol:
    def __init__(self,path):
        self.data = {}
        self.running = 0
        self.path = path
        
        with open(self.path,'r') as f:
            for i, lines in enumerate(f.readlines()):
                k,v = lines.split(':')
                self.data[i] = {'key': int(k), 'values': v.strip().split()}

    @staticmethod
    def lrevaluator(target,string):
        
        worker = re.split(r'([\+\*])',string)
        accum = worker[0]
        for w in range(1,len(worker)):
            accum += worker[w]
            if worker[w].isdigit():
                accum = str(eval(accum))
        if int(accum) == target:
            return True
        else:
            return False
    
    def solve(self):
        two = ['+','*']
        for _,k in self.data.items():
            target = k['key']
            it = k['values']
            n = len(it)-1
            operators = list(product(two, repeat=n))
            
            for o in operators:
                st = '' 
                for j in range(n):
                    st += it[j] + o[j]
                
                st += it[n]
                
                
                if self.lrevaluator(target,st):
                    self.running += int(target)
                    break
                    
        return self.running
