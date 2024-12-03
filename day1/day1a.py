class AOC1aSol:
    def __init__(self, p):
        self.path = p
        self.list1 = []
        self.list2 = []
    
        with open(self.path,'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                rr = re.findall(r'(\d{5})',line[0])
                if rr:
                    self.list1.append(int(rr[0]))
                    self.list2.append(int(rr[1]))
        
    def getsol(self):
        accrue = 0
        self.list1.sort()
        self.list2.sort()
        for l in range(len(self.list1)):
            accrue += abs(self.list1[l]-self.list2[l])
        
        return accrue
