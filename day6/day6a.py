#day6a
class AOC6aSol:
    def __init__(self, p):
        self.path = p
        self.board = []
        self.pointer = (0, 0)
        self.pointtype = '?'
        self.tofind = ['<', '>', '^', 'v']
        self.collen = 0
        self.rowlen = 0
        self.visited = set()

        with open(self.path, 'r') as f:
            for i, line in enumerate(f.readlines()):
                row = list(line.strip('\n'))  
                self.board.append(row)
                for j, c in enumerate(row):
                    if c in self.tofind:
                        self.pointer = (i, j)
                        self.pointtype = c
                        
        self.rowlen = len(self.board)
        self.collen = len(self.board[0]) if self.rowlen > 0 else 0

    def movement(self):
        
        turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        move = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

        
        next_move = move[self.pointtype]
        next_space = (self.pointer[0] + next_move[0], self.pointer[1] + next_move[1])

        
        if (next_space[0] < 0 or next_space[0] >= self.rowlen or
                next_space[1] < 0 or next_space[1] >= self.collen):
            return False  
            #out of bounds, game over

        
        if self.board[next_space[0]][next_space[1]] != '.':
            self.pointtype = turns[self.pointtype]  
        else:
            self.pointer = next_space
            self.visited.add(next_space)

        return True 

    def solve(self):
     
        self.visited.add(self.pointer)

       
        while self.movement():
            pass

        return len(self.visited)
