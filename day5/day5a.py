import re

class AOC5aSol:
    def __init__(self, p):
        self.path = p
        self.dict = {}
        self.ordered = []
        self.middletrack = 0

        with open(self.path, 'r') as f:
            for l in f.readlines():
                dic = re.findall(r'(\d+)\|(\d+)', l)
                if dic:
                    one, two = int(dic[0][0]), int(dic[0][1])
                    if self.dict.get(one, 99999) == 99999:
                        self.dict[one] = [two]
                    else:
                        self.dict[one].append(two)
                else:
                    for ls in l.split('\n'):
                        if ls != '':
                            self.ordered.append(list(int(g) for g in ls.split(',')))

    def check(self, target):
        lt = len(target)
        for j in range(lt - 1, -1, -1):  
            values = self.dict.get(target[j], [])
            for t in values:
                if t in target[:j]: 
                    return False

        middle_index = len(target) // 2
        self.middletrack += target[middle_index]
        return True

    def getsol(self):

        for gs in self.ordered:
            self.check(gs)
        return self.middletrack
