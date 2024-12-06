class AOC4bSol:
    def __init__(self, p):
        self.path = p
        self.countxmas = 0
        self.dest = []
    
        
        with open(self.path, 'r') as f:
            for l in f.readlines():
                self.dest.append(l.strip('\n'))
    
        self.maxi = len(self.dest)  
        self.maxj = len(self.dest[0])

    def getsol(self):
        #check all 3x3 matrices
        for r in range(0, self.maxi - 2):  
            for c in range(0, self.maxj - 2):  
              
                submatrix = [
                    self.dest[i][c:c + 3]
                    for i in range(r, r + 3)
                ]

               
                if len(submatrix) == 3 and all(len(row) == 3 for row in submatrix):
                    
                    if submatrix[1][1] == 'A':  
                        
                        top_left = submatrix[0][0] + submatrix[1][1] + submatrix[2][2]
                        top_right = submatrix[0][2] + submatrix[1][1] + submatrix[2][0]

                        
                        if top_left in {"MAS", "SAM"} and top_right in {"MAS", "SAM"}:
                            self.countxmas += 1
        return self.countxmas
