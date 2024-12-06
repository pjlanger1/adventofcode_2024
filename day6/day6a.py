#day6a
path = '/Users/peter/Downloads/aoc6a.txt'

class AOC6aSol:
    def __init__(self, p):
        self.path = p
        self.board = []
        self.pointer = 0
        self.pointtype = '?'
        self.tofind = ['<','>','^','v']
        self.collen = 0
        self.rowlen = 0
        self.pos = set()
        
        with open(self.path, 'r') as f:
            i = 0
            for l in f.readlines():
                self.board.append(list(l))
                j = 0
                for c in l:
                    if c in self.tofind:
                        self.pointer = (i,j) 
                        self.pointtype = c
                    j += 1
                i += 1
                
        self.collen = len(self.board[0])
        self.rowlen = len(self.board)
    
    def movement(self):
        turns = {'^':'>','>':'v','v':'<','<':'^'}
        move = {'^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1)}
        
        nextmove = move[self.pointtype]
        nextspace = (self.pointer[0]+nextmove[0],self.pointer[1]+nextmove[1])
        
        if nextspace[0] < 0 or nextspace[0] >= self.rowlen or nextspace[1] < 0 or nextspace[1] >= self.collen:
            print('game over!')
            self.pointer = (-1, -1)  
            return
        
        elif self.board[nextspace[0]][nextspace[1]] != '.':
            self.pointtype = turns[self.pointtype]
        
        else:
            self.pointer = nextspace
    
    def gameover(self):
        return self.pointer[0] < 0 or self.pointer[1] < 0
    
    def solve(self):
        while not self.gameover():
            self.pos.add(self.pointer)
            self.movement()
        
        return len(self.pos)
            
        
            
