import random
class SnakeLadder:
    update = 1
    snake = {}
    ladder = {}
    prevpos = 1
    pos = 1
    val = 1
    mainboard = []
    for i in range(5):
        temp = []
        for j in range(10):
            temp.append(val)
            val += 1
        mainboard.append(temp)
    def __init__(self):
        #using constructor to design the board
        #generating ladders 
        for l in range(5):
            t1 = random.randrange(1,50)
            if(t1 not in self.ladder):
                self.ladder[t1] = random.randrange(t1,50)
            else:
                continue
        #generating snakes
        for s in range(5):
            s1 = random.randrange(1,50)
            if s1 not in self.snake and s1 not in self.ladder:
                self.snake[s1] = random.randrange(1,s1)
            else:
                continue
        print(self.ladder)
        print(self.snake)
        self.game()
    def board(self):
        #method used to update board
        col = self.pos // 10
        row = self.pos % 10
        col1 = self.prevpos // 10
        row1 = self.prevpos % 10
        self.mainboard[col1][row1] = self.prevpos + 1
        self.mainboard[col][row] = "<.>"
        for _ in self.mainboard:
            print(_)
    def snake_bite(self):
        
        self.prevpos = self.pos
        self.pos = self.snake[self.pos]
        print(f"Snake from {self.prevpos} to {self.pos}")
        self.board()
    def ladder_climb(self):
        self.pos = self.ladder[self.pos]
        print(f"Ladder from {self.prevpos} to {self.pos}")
        self.board()    
    def game(self):
        if(self.pos <= 1):
            for row in self.mainboard:
                print(row)
        play = True
        while play and self.pos < 50:
            inp = int(input(">> 1.Roll \n>>2.Quit \n"))
            if(inp == 1):
                roll = random.randrange(1,6)
                print(f"DIE ROLL = {roll}")
                self.prevpos = self.pos
                self.pos += roll
                if(self.pos >= 50):
                    print("Congrats you won")
                    return
                if(self.pos in self.ladder):
                    self.ladder_climb()
                elif(self.pos in self.snake):
                    self.snake_bite()
                else:
                    self.board()
            elif(inp == 2):
                play = False
            else:
                print("Return a valid value")
        print("Thank you for playing")
        self.__init__()
letsplay = SnakeLadder()


        

        