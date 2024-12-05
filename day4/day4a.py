class AOC4aSol:
    def __init__(self, p):
        self.path = p
        self.countxmas = 0
        self.dest = []
    
        
        with open(self.path, 'r') as f:
            for l in f.readlines():
                self.dest.append(l.strip('\n'))
    
        self.maxi = len(self.dest)  
        self.maxj = len(self.dest[0])  

    def check_position(self, i, j):
       
        directions = {
            "horizontal": [(0, 1), (0, -1)],  
            "vertical": [(1, 0), (-1, 0)],  
            "right_diagonal": [(1, 1), (-1, -1)],  
            "left_diagonal": [(1, -1), (-1, 1)]   
        }

        for k, v in directions.items():
            for r, c in v:
                substring = self.extract_string(i, j, r, c)
                if substring:
                    self.countxmas += self.count_occurrences(substring, "XMAS")
        return None

    def extract_string(self, i, j, dr, dc):
        """
        Extract a string from the grid starting at (i, j) in direction (dr, dc).
        """
        chars = []
        for n in range(4):  #extract up to 4 characters
            ni, nj = i + dr * n, j + dc * n
            if 0 <= ni < self.maxi and 0 <= nj < self.maxj:
                chars.append(self.dest[ni][nj])
            else:
                return None  #stop if out of bounds
        return ''.join(chars)

    @staticmethod
    def count_occurrences(string, substring):
        """
        Counts all occurrences of a substring in a string, including overlaps.
        """
        count = 0
        start = 0
        while True:
            start = string.find(substring, start)
            if start == -1:  #no more occurrences
                break
            count += 1
            start += 1  #move one step forward to allow overlaps
        return count

    def getsol(self):
        #check all grid positions
        for r in range(self.maxi):
            for c in range(self.maxj):
                self.check_position(r, c)
        return self.countxmas
